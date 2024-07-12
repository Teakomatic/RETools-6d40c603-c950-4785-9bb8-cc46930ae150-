from Rhino.Geometry import PolyCurve

def ease(self, amount=0.1):
    """Pick points close but distinct from a curve's ends.

    Split a multi-segment curve into segments.
    Ease each end point 10% along its containing segment.

    Args:
        amount (float, optional): Easing amount. Defaults to 0.1.

    Returns:
        [Point]: A pair of eased end points.
    """
    p = PolyCurve()
    p.Append(self)
    p.RemoveNesting()
    first_segment = p.SegmentCurve(0)
    last_segment = p.SegmentCurve(p.SegmentCount - 1)
    eased_first = first_segment.PointAtNormalizedLength(amount)
    eased_last = last_segment.PointAtNormalizedLength(1 - amount)
    return eased_first, eased_last
