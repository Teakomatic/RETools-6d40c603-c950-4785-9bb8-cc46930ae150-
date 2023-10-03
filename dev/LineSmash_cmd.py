"""
The LineSmash command.

This command smashes selected curves into a single line,
and deletes the original curves.
"""

from Rhino.Geometry.Line import TryFitLineToPoints

from command import SUCCESS, FAILURE
from services.doc_objects import AddCurve, DocObjects
from geometry import sample, DeformableLine
from services.log import info


def RunCommand(is_interactive):
    """Linesmash selected curves."""

    # Grab selected items
    objects = DocObjects.GetSelected()

    # Fail soft for empty selection
    if not objects:
        info("No items selected. Doing nothing.")
        return SUCCESS

    # Report selection
    info("selected {} curves and {} points".format(len(objects.curves), len(objects.points)))

    # Preprocess objects into points
    points = sample(objects)

    # Fail soft for single point sample
    if len(points) == 1:
        info("Only one point in input sample. Doing nothing.")
        return SUCCESS

    # Fit geometry
    info("Fitting line to {} points.".format(len(points)))
    success, line = TryFitLineToPoints(points)

    # Fail hard on fit failure
    if not success:
        info("Line Fit Error: Fit operation has failed")
        return FAILURE

    # Generate a deformable line
    line = DeformableLine(line)

    # Add generated geometry to document
    AddCurve(line)

    # Delete input geometry
    info("Deleting inputs.")
    objects.delete()

    return SUCCESS
