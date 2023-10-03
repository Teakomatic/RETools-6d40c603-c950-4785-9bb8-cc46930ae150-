"""
/RETools/dev/services/import_tools.py
(c) 2023 Mars Industrial (AGPLv3)

This module contains tools for importing DXF files into Rhino.

Usage:
import_dxfs(folder, border=20)

Effects:
- Imports DXF files from the current job directory into the open .3dm file.
- Arrange large 2d items horizontally, small 2d items vertically, and 3d items to the left.
"""

import scriptcontext as sc
import rhinoscriptsyntax as rs
from Rhino.Geometry import Point3d

from conf import TEXT_HEIGHT, TEXT_HEIGHT_3D, SHORT_ITEM_LENGTH
from file import name, get_dxfs_recursive, current_folder
from rhino import bbox, silent, text_centered, text_centered_vertical
from log import info, debug


def import_dxf(file):
    """
    Import a single dxf file.

    Note: Requires user to set default DXF import settings
    """

    debug("Importing {}".format(file))

    command = '-import "{}" enter'.format(file)

    silent(command)

    sel = rs.SelectedObjects()

    silent("selnone")

    return sel


class Import:
    def __init__(self, dxf):
        # Import document
        self.object = import_dxf(dxf)

        # Process import metadata
        self.name = name(dxf)
        self.update_metadata()

        # Align import centerline to y axis
        self.move(-self.base)

    def move(self, vector):
        rs.MoveObjects(self.object, vector)
        self.update_metadata()

    def update_metadata(self):
        box = self.box
        self.length = box.Diagonal.Y
        self.width = box.Diagonal.X
        self.mid = self.width / 2
        self.area = box.Area
        self.is_2d = box.IsDegenerate(sc.doc.ModelAbsoluteTolerance)
        self.corner = box.Min
        self.center = box.Min + box.Diagonal / 2
        self.base = box.Min + Point3d(self.mid, 0, 0)

    @property
    def box(self):
        return bbox(self.object)


def label_2d_item(item, spacing):
    # Name item below, centered
    position = (item.base.X, item.base.Y - spacing)
    text_centered(item.name, TEXT_HEIGHT, position)


def label_small_2d_item(item, spacing):
    # Name item right, centered
    position = item.base.X + item.mid + spacing, item.base.Y + item.length / 2
    text_centered_vertical(item.name, TEXT_HEIGHT, position)


def label_3d_item(item, spacing):
    # Name item below, centered
    name_position = item.base.X, item.base.Y - spacing
    text_centered(item.name, TEXT_HEIGHT, name_position)
    # Mark 3d item on center
    marker_position = item.center.X, item.center.Y
    text_centered("3D", TEXT_HEIGHT_3D, marker_position)


def import_dxfs(source_folder, border):
    half_border = border / 2

    import_items = get_dxfs_recursive(source_folder)

    # Report items
    if not import_items:
        info("No items to import. Doing nothing.")
        return

    info("Importing {} items:".format(len(import_items)))
    for dxf in import_items:
        info(name(dxf))

    # Import  and preprocess item metadata
    _3d_imports = []
    _2d_imports = []
    for dxf in import_items:
        item = Import(dxf)

        # Sort imports by 2d/3d status
        if item.is_2d:
            _2d_imports.append(item)
        else:
            _3d_imports.append(item)

    # Sort imports by size
    by_area = lambda item: item.area
    _2d_imports.sort(key=by_area, reverse=True)
    _3d_imports.sort(key=by_area, reverse=True)

    # Split short and long 2d imports
    _2d_imports_long = [x for x in _2d_imports if x.length >= SHORT_ITEM_LENGTH]
    _2d_imports_short = [x for x in _2d_imports if x.length < SHORT_ITEM_LENGTH]

    # Arrange and label 2d imports
    base_point_2d = Point3d.Origin
    first_long_2d_item = True

    # Align large 2d items horizontally to right of origin
    for item in _2d_imports_long:
        # Leave first 2d item on midline
        if first_long_2d_item:
            first_long_2d_item = False

        # Accomodate left side of subsequent items
        else:
            base_point_2d.X += item.mid

        item.move(base_point_2d)

        label_2d_item(item, spacing=half_border)

        # Accomodate right side of object
        base_point_2d.X += item.mid

        #  Invariant: Offset point is now at right end of item

        # Add a border
        base_point_2d.X += border

    # Align small 2d items vertically to right of large items

    for item in _2d_imports_short:
        # Accomodate left side of item
        item.move(base_point_2d + Point3d(item.mid, 0, 0))

        label_small_2d_item(item, spacing=half_border)

        # Accomodate item length
        base_point_2d.Y += item.length

        # Invariant: Offset is now at top end of item

        # Add border
        base_point_2d.Y += border

    # Report bad imports with short placeholders

    # Arrange and label 3d imports
    base_point_3d = Point3d.Origin

    # Shift 3d base point to avoid 2d imports
    if _2d_imports_long:
        base_point_3d.X -= _2d_imports_long[0].mid + border
    elif _2d_imports_short:
        base_point_3d = _2d_imports_short[0].corner
        base_point_3d.X -= _2d_imports_short[0].mid

    # Align 3d items horizontally to the left
    for item in _3d_imports:
        # Accomodate right end of item
        base_point_3d.X -= item.mid

        item.move(base_point_3d)

        label_3d_item(item, spacing=half_border)

        # Accomodate left end of item
        base_point_3d.X -= item.mid

        # Invariant: Offset point is now at left end of item

        # Add border between items
        base_point_3d.X -= border


if __name__ == "__main__":
    folder = current_folder()
    import_dxfs(folder, border=20)