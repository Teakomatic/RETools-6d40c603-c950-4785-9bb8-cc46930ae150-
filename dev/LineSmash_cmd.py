"""
The LineSmash command.

This command smashes selected curves into a single line,
and deletes the original curves.
"""

from Rhino.Geometry.Line import TryFitLineToPoints

from geometry import sample, DeformableLine
from services import doc_objects, log

def RunCommand(is_interactive):
    """Linesmash selected curves."""

    # Grab selected items
    objects = doc_objects.get_selected()

    # Fail soft for empty selection
    if not objects:
        log.info("No items selected. Doing nothing.")
        return 0

    # Report selection
    log.info("selected {} curves and {} points".format(len(objects.curves), len(objects.points)))

    # Preprocess objects into points
    points = sample(objects)

    # Fail soft for single point sample
    if len(points) == 1:
        log.info("Only one point in input sample. Doing nothing.")
        return 0

    # Fit geometry
    log.info("Fitting line to {} points.".format(len(points)))
    success, line = TryFitLineToPoints(points)

    # Fail hard on fit failure
    if not success:
        log.info("Line Fit Error: Fit operation has failed")
        return 1

    # Generate a deformable line
    line = DeformableLine(line)

    # Add generated geometry to document
    doc_objects.add_curve(line)

    # Delete input geometry
    log.info("Deleting inputs.")
    objects.delete()

    return 0
