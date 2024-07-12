QUARTER_INCH = 0.25


def sample(objects, sampling_distance=QUARTER_INCH):
    """
    Sample a pointcloud from a collection of document objects.

    Args:
        objects: DocObjects. Points and curves to sample.
        sampling_distance: float. The length between sample points.

    Returns:
        list[Point3d]. A list of point samples.
    """

    # Alert if given no geometry
    if not objects:
        raise Exception("Sampler Error: Empty input.", objects)

    # Turn doc Points into Point3ds
    samples = [pt.Geometry.Location for pt in objects.points]

    # Sample curve end points and interiors
    for curve in objects.curves:
        curve = curve.Geometry
        start = curve.PointAtStart
        end = curve.PointAtEnd
        if start != end:
            samples += [start, end]
        else:
            samples.append(start)

        ts = curve.DivideByLength(sampling_distance, False)
        if ts:
            samples += [curve.PointAt(t) for t in ts]

    # Alert if sampled zero points
    if not samples:
        raise Exception("Sampler Error: Zero Points sampled.", objects)

    return samples
