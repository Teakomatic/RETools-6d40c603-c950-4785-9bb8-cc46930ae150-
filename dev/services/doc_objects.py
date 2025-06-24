"""
This module contains functions for interacting with Rhino's
document and docobjects.
"""

import functools
from scriptcontext import doc
import rhinoscriptsyntax as rs
from services import log

# Rhino document object types
POINT = 1
CURVE = 4


class DocObjects:
    def __init__(self, items):
        self.curves = []
        self.points = []
        self.others = []

        for item in items:
            type = rs.ObjectType(item)
            if type == CURVE:
                self.curves.append(item)
            elif type == POINT:
                self.points.append(item)
            else:
                log.info("Warning: Selected nonstandard geometry")
                self.others.append(item)

    def __nonzero__(self):
        return self.curves or self.points or self.others

    def __iter__(self):
        return iter(self.points + self.curves)

    def delete(self):
        delete_objects(self.points + self.curves + self.others)
        self.curves = []
        self.points = []
        self.others = []

    def transform(self, xform):
        for item in self:
            doc.Objects.Transform(item, xform, deleteOriginal=True)


# Adding geometry to document
add_curve = doc.Objects.AddCurve
add_curves = functools.partial(map, add_curve)
add_circle = doc.Objects.AddCircle
add_line = doc.Objects.AddLine
add_point = doc.Objects.AddPoint

# Selection tools
deselect_all = doc.Objects.UnselectAll
get_selected = lambda: DocObjects(doc.Objects.GetSelectedObjects(False, False))

# Deleting objects
delete_objects = functools.partial(map, doc.Objects.Delete)
