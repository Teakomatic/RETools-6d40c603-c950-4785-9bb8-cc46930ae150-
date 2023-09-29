"""
This command will attemp to fillet the currently selected curve or pair of curves.

The command queries a repo for radius information. 

This command is intended to be used with a user facing radius controller interface.

In debug mode, we mark the starting points that we give to the native fillet command.

We fail soft for all errors, so that we do not interupt the repeat/* macro
"""

from Rhino.Geometry.Curve import CreateFilletCurves
from Rhino.Geometry import Point3d
from scriptcontext import doc
from Rhino.Collections import Point3dList

from services.log import info

from command import SUCCESS
from doctools import DocObjects, AddPoint, AddLine
from geometry import closest, ease
from repo import radius_repo

DEBUG = False

FILLET_OPTIONS = {
    "join": True,
    "trim": True,
    "arcExtension": True,
    "tolerance": doc.ModelAbsoluteTolerance,
    "angleTolerance": doc.ModelAngleToleranceDegrees,
}


def RunCommand(is_interactive):
    # Fetch current radius
    FILLET_OPTIONS["radius"] = radius_repo.get()
    info("Current radius is {}".format(FILLET_OPTIONS["radius"]))

    # Get selected curve geometry
    curve_docobjects = DocObjects.GetSelected().curves
    curves = [item.Geometry for item in curve_docobjects]
    n = len(curves)

    # Fail soft for invalid selection
    if n not in {1, 2}:
        info("Please select one or two curves. {} selected.".format(n))

        # Deselect if 3+ objects selected
        if n > 2:
            doc.Objects.UnselectAll()

        return SUCCESS

        # n = 1: Keep object selected in case self fillet fails
        # This allows user to select a second object on next attempt

    # Setup a two curve fillet
    if len(curves) == 2:
        crv_A, crv_B = curves
        # find the closest pair of starting points
        ps, qs = ease(crv_A), ease(crv_B)
        p, q = closest(ps, qs)

    # Setup a self fillet
    if len(curves) == 1:
        crv_A = crv_B = curves[0]
        p, q = ease(crv_A)

    # Perform fillet
    fillet = CreateFilletCurves(crv_A, p, crv_B, q, **FILLET_OPTIONS)

    if DEBUG:
        # Mark fillet initial conditions
        AddPoint(p)
        AddPoint(q)
        AddLine(p, q)

    # Fail soft if fillet failed
    if not fillet:
        # Deselect inputs if failed with two curves
        if len(curves) == 2:
            DocObjects.DeselectAll()
        info("Fillet Failed")
        return SUCCESS

    # Add filleted geometry
    for curve in fillet:
        doc.Objects.AddCurve(curve)

    # Tidy old geometry
    for curve in curve_docobjects:
        doc.Objects.Delete(curve)

    return SUCCESS


if __name__ == "__main__":
    RunCommand(True)
