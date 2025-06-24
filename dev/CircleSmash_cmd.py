"""
The CircleSmash command.

This command smashes selected curves into a single circle,
and deletes the original curves.
"""

from Rhino.Geometry.Circle import TryFitCircleToPoints

from geometry import sample
from services import doc_objects, log

def RunCommand(is_interactive):
    """Circlesmash selected curves."""

    # Grab selected items
    objects = doc_objects.get_selected()

    # Fail soft for empty selection
    if not objects:
        log.info("No items selected. Doing nothing.")
        return 0

    # Report selection
    log.info(
        "Selected {} curves and {} points".format(
            len(objects.curves), len(objects.points)
        )
    )

    # Preprocess objects into points
    points = sample(objects)

    # Fail soft for single point sample
    if len(points) == 1:
        log.info("Only one point in input sample. Doing nothing.")
        return 0

    # Fit geometry
    log.info("Fitting circle to {} points.".format(len(points)))
    success, circle = TryFitCircleToPoints(points)

    # Fail hard on fit failure
    if not success:
        log.info("Circle Fit Error: Fit operation has failed")
        return 1

    # Add generated geometry to document
    doc_objects.add_circle(circle)

    # Delete input geometry
    log.info("Deleting curves.")
    objects.delete()

    return 0
