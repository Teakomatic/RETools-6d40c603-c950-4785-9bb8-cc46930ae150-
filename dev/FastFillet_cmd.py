from Rhino.Geometry.Curve import CreateFilletCurves as Fillet
from dev.doctools import DocObjects
from scriptcontext import doc
from Rhino.Geometry import PolyCurve
from rhinoscriptsyntax import ObjectType


# Generate diagnostic geometry for easing step
DEBUG = False

# Rhino fillet operation options
FILLET_OPTIONS = {
    "join": True,
    "trim": True,
    "arcExtension": True,
    "tolerance": doc.ModelAbsoluteTolerance,
    "angleTolerance": doc.ModelAngleToleranceDegrees,
    "radius": 0.25,
}


def closest(self, other):
    return min(
        [(a, b) for a in self for b in other],
        key=lambda ab: ab[0].DistanceToSquared(ab[1]),
    )


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


def fast_fillet():
    # Get selected curve geometry
    curve_docobjects = DocObjects.GetSelected().curves
    curves = [item.Geometry for item in curve_docobjects]
    n = len(curves)

    # Validate selection
    if n not in {1, 2}:
        print("Please select one or two curves. {} selected.".format(n))

        # Deselect if 3+ objects selected
        if n > 2:
            doc.Objects.UnselectAll()
        exit()

        # n = 1: Keep object selected in case self fillet fails
        # This allows user to select a second object on next attempt

    # Perform a two curve fillet
    if len(curves) == 2:
        fillet_input_A, fillet_input_B = curves
        p, q = ease(fillet_input_A), ease(fillet_input_B)
        p, q = closest(p, q)

    # Perform a self fillet
    if len(curves) == 1:
        fillet_input_A = fillet_input_B = curves[0]
        p, q = ease(fillet_input_A)

    fillet = Fillet(fillet_input_A, p, fillet_input_B, q, **FILLET_OPTIONS)

    if DEBUG:
        doc.Objects.AddPoints([p, q])
        doc.Objects.AddLine(p, q)

    # Fail soft if fillet failed
    if not fillet:
        # Deselect inputs if failed with two curves
        if len(curves) == 2:
            DocObjects.DeselectAll()
        print("Fillet Failed")
        exit()

    # Add filleted geometry
    for curve in fillet:
        doc.Objects.AddCurve(curve)

    # Tidy old geometry
    for curve in curve_docobjects:
        doc.Objects.Delete(curve)


def RunCommand(is_interactive):
    fast_fillet()
