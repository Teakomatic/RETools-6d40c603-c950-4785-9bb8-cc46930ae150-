"""
 A collection of functions for working with Rhino.Geometry.Point3d
"""


def interpolate(
    a, b, t
):  # Type: Rhino.Geometry.Point3d, Rhino.Geometry.Point3d, float -> Rhino.Geometry.Point3d
    """
    Interpolate between two points.

    Args:
        a: Rhino.Geometry.Point3d. A point.
        b: Rhino.Geometry.Point3d. A point.
        t: float. A parameter.

    Returns:
        Rhino.Geometry.Point3d. A point.
    """
    a_b = b - a  # Type: Rhino.Geometry.Vector3d
    return a + t * a_b
