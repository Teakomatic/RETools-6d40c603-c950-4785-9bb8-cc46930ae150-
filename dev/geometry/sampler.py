QUARTER_INCH = 0.25


def sample_pointcloud_from_curves(curves, sampling_distance=QUARTER_INCH):
    """
    Sample a pointcloud from a collection of curves.

    Sampling happens by dividing the curve into segments of a uniform length
    and sampling the points at each division.

    Args:
        curves: Rhino.Geometry.Curve[]. A list of curves to sample points from.
        sampling_distance: float. The length of each segment to divide the curve into.

    Returns:
        list. A list of points sampled from the input curves.
    """

    sample_points = []  # Type: Rhino.Geometry.Point3d

    for curve in curves:  # Type: Rhino.Geometry.Curve
        # Sample start and end points of the curve
        sample_points += [curve.PointAtStart, curve.PointAtEnd]

        # Divide the curve by length to get additional sample points
        sample_points += [
            curve.PointAt(t) for t in curve.DivideByLength(sampling_distance, False)
        ]

    return sample_points
