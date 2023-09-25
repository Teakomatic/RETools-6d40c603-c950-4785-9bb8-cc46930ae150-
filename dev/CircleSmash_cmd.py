"""
The CircleSmash command.

This command smashes selected curves into a single circle,
and deletes the original curves.
"""

from Rhino.Geometry.Circle import TryFitCircleToPoints

from command import SUCCESS, FAILURE
from doctools import AddCircle, DocObjects
from geometry import sample
from services.log import info


def RunCommand(is_interactive):
    """Circlesmash selected curves."""

    # Grab selected items
    objects = DocObjects.GetSelected()

    # Fail soft for empty selection
    if not objects:
        info("No items selected. Doing nothing.")
        return SUCCESS

    # Report selection
    info(
        "Selected {} curves and {} points".format(
            len(objects.curves), len(objects.points)
        )
    )

    # Preprocess objects into points
    points = sample(objects)

    # Fail soft for single point sample
    if len(points) == 1:
        info("Only one point in input sample. Doing nothing.")
        return SUCCESS

    # Fit geometry
    info("Fitting circle to {} points.".format(len(points)))
    success, circle = TryFitCircleToPoints(points)

    # Fail hard on fit failure
    if not success:
        info("Circle Fit Error: Fit operation has failed")
        return FAILURE

    # Add generated geometry to document
    AddCircle(circle)

    # Delete input geometry
    info("Deleting curves.")
    objects.delete()

    return SUCCESS
