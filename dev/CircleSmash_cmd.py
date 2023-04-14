"""
Circle Smash Command

This command smashes selected curves into a single circle,
and deletes the original curves.
"""

from doctools import AddCircle, Delete, Geometry, GetSelectedCurves
from geometry.fit import CircleFit


def RunCommand(is_interactive):
    """Circlesmash selected curves."""

    curves = GetSelectedCurves()  # Type: Rhino.Doc.DocObject<Curve>
    print("Selected curves: {}".format(len(curves)))

    if not curves:
        print("No curves selected.")
        return 1

    print("Fitting circle to curves.")

    curve_geometry = Geometry(curves)  # Type: Rhino.Geometry.Curve[]
    print("Curve geometry: {}".format(len(curve_geometry)))

    circle = CircleFit(curve_geometry)  # Type: Rhino.Geometry.Circle
    print("Circle geometry: {}".format(circle))

    AddCircle(circle)

    print("Deleting curves.")
    Delete(curves)

    return 0
