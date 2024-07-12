"""A collection of functions for working with Rhino.Geometry.Line"""

from Rhino.Geometry.Curve import CreateControlPointCurve

from interpolate import interpolate


def DeformableLine(input):  # Type: Line, Iterable[float] -> Curve
    """
    Create a deformable curve from a Rhino.Geometry.Line

    Args:
        input: Line. A line to rebuild.

    Returns:
        Curve. A straight control point curve.
    """
    start, end = (
        input.From,
        input.To,
    )  # Point3d, Point3d

    control_points = [
        interpolate(start, end, t) for t in (0, 0.125, 0.5, 0.875, 1)
    ]  # :list[Point3d]

    return CreateControlPointCurve(control_points, degree=3)
