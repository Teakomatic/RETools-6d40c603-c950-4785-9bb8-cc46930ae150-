"""A collection of functions for working with Rhino.Geometry.Line"""

from Rhino.Geometry.Curve import CreateControlPointCurve

from point import interpolate


def DeformableLine(
    line, t_params=(0, 1 / 8.0, 1 / 2.0, 7 / 8.0, 1)
):  # Type: Rhino.Geometry.Line, Iterable[float] -> Rhino.Geometry.Curve
    """
    Create a deformable curve from a Rhino.Geometry.Line

    Args:
        line: Rhino.Geometry.Line. A line to rebuild.

    t_params: Iterable of float. A list of t parameters to use for control points.
        By default, the curve has five control points spaced at 0, 1/8, 1/2, 7/8, 1 of the line length.

    Returns:
        Rhino.Geometry.Curve. A straight control point curve.
    """
    start, end = (
        line.From,
        line.To,
    )  # Type: Rhino.Geometry.Point3d, Rhino.Geometry.Point3d

    control_points = [
        interpolate(start, end, t) for t in t_params
    ]  # Type: List[Rhino.Geometry.Point3d]

    return CreateControlPointCurve(control_points, degree=3)
