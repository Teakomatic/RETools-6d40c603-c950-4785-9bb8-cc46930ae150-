"""
Line Smash Command

The command name is defined by the filname minus "_cmd.py"

"""

from doctools import AddCurve, Delete, Geometry, GetSelectedCurves
from geometry.fit import LineFit


def RunCommand(is_interactive):
    """Linesmash selected curves."""
    print("Line Smash")
    curves = GetSelectedCurves()  # Type: Rhino.Doc.DocObject<Curve>
    print("Selected curves: {}".format(len(curves)))

    if not curves:
        print("No curves selected.")
        return 1

    print("Fitting line to curves.")
    curve_geometry = Geometry(curves)  # Type: Rhino.Geometry.Curve[]
    print("Curve geometry: {}".format(len(curve_geometry)))
    line = LineFit(curve_geometry, type="deformable")  # Type: Rhino.Geometry.Curve
    print("Line geometry: {}".format(line))
    AddCurve(line)

    print("Deleting curves.")
    Delete(curves)

    return 0
