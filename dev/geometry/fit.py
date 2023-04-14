from Rhino.Geometry.Circle import TryFitCircleToPoints
from Rhino.Geometry.Line import TryFitLineToPoints
from geometry.line import DeformableLine

from geometry.sampler import sample_pointcloud_from_curves

# Fitting configuration (TODO: use these / eliminate these)
ENDS = True  # Include curve endpoints
VERTEX = False  # Include polyline vertices
SEGMENT = True  # Divide curves by length
DELETE = True  # Delete input curves


def CircleFit(curves):  # Type: Rhino.Geometry.Curve[] -> Rhino.Geometry.Circle
    """
    Find the best-fit circle for a list of curves.

    Args:
        curves: Rhino.Geometry.Curve[]. A list of curves to find the best-fit circle.

    Returns:
        Rhino.Geometry.Circle. The best-fit circle for the input curves.
    """

    if not curves:
        raise ValueError("CircleFit called with empty argument")

    points = sample_pointcloud_from_curves(curves)  # Type: Rhino.Geometry.Point3d[]

    success, circle = TryFitCircleToPoints(points)

    if not success:
        raise Exception("CircleFit operation has failed")

    return circle


def LineFit(curves, type=""):  # Type: Rhino.Geometry.Curve[] -> Rhino.Geometry.Line
    """
    Find the best-fit line for a list of curves.

    Args:
        curves: Rhino.Geometry.Curve[]. A list of curves to find the best-fit line.

    Returns:
        Rhino.Geometry.Line. The best-fit line for the input curves.
    """

    if not curves:
        raise ValueError("LineFit called with empty argument")

    points = sample_pointcloud_from_curves(curves)  # Type: Rhino.Geometry.Point3d[]

    success, line = TryFitLineToPoints(points)

    if not success:
        raise Exception("LineFit operation has failed")

    if type == "deformable":
        line = DeformableLine(line)

    return line
