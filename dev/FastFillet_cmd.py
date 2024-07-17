"""
This command will attemp to fillet the currently selected curve or pair of curves.

The command queries a repo for radius information. 

This command is intended to be used with a user facing radius controller interface.

In debug mode, we mark the starting points that we give to the native fillet command.

We fail soft for all errors, so that we do not interupt the repeat/* macro
"""

from Rhino.Geometry.Curve import CreateFilletCurves
from scriptcontext import doc

from command import SUCCESS
from services.log import info, error, debug
from geometry import closest, ease
from repo import radius_repo
from services import doc_objects

DEBUG = False

FILLET_OPTIONS = {
    "join": True,
    "trim": True,
    "arcExtension": True,
    "tolerance": doc.ModelAbsoluteTolerance,
    "angleTolerance": doc.ModelAngleToleranceDegrees,
}


class InvalidSelection(Exception):
    """
    Exception for invalid selection

    This means:
    - No objects selected
    - More than two objects selected   
    """
    pass


class FilletFailure(Exception):
    """
    Exception for fillet failure

    This means:
    - Self fillet failed
        - The curve is a line
        - The curve is closed
        - The ends are coplanar
    - Two curve fillet failed
        - The fillet radius is too large
        - The fillet starting points diverge
    """
    pass


class FailSoft(Exception):
    """
    Exception for soft failure
    
    This exception is used to indicate that the operation failed, but that
    the command should not be aborted. This is used to allow the repeat
    command to continue to the next iteration.
    """
    pass


def select_curves():
    """
    Select the curves to fillet

    Returns:
        tuple[list[curve], int]: The selected curves and the number of curves
    """
    # User Prompt for Curve Selection (Currently automatic)
    doc_curves = doc_objects.get_selected().curves
    curves = [item.Geometry for item in doc_curves]
    n = len(curves)

    # Selection Validation
    if n not in {1, 2}:
        info("Please select one or two curves. {} selected.".format(n))

        # Deselect if 3+ objects selected
        if n > 2:
            doc_objects.UnselectAll()

        # n = 1: Keep object selected in case self fillet fails
        # This allows user to select a second object on next attempt

        raise FailSoft(InvalidSelection)

    return curves, doc_curves, n


def get_radius():
    """
    Get the radius for the fillet operation

    Returns:
        float: The radius for the fillet operation
    """
    while True:
        try:
            # Radius Input Dialog
#            rs.GetReal("Enter the fillet radius.", 0)
            info("Enter the radius of the circle.")
            radius_input = input("Radius: ")
            debug("radius_input type: {}".format(type(radius_input)))

            # Input Conversion
            if type(radius_input) in {float, int}:
                radius = radius_input

            elif isinstance(radius_input, str):
                radius = float(radius_input.strip())

        # Input Validation
        except ValueError:
            error("Invalid input. Please enter a valid number.")
            continue

        except Exception as e:
            error("Input Error: {}. Using default radius".format(e))
            debug("Error type: {}".format(type(e)))
            radius = 0

        if radius < 0:
            error("Radius must be a positive number or zero.")
            continue

        break

    # Repository Radius Fetch (if applicable)
    if radius == 0:
        radius = radius_repo.get()

    info("Current radius: {}".format(radius))
    return radius


def perform_fillet(curves, n, radius):
    """
    Perform the fillet operation

    Args:
        curves (list): The curves to fillet
        n (int): The number of curves to fillet
        radius (float): The radius of the fillet

    Returns:
        list[curve]: The fillet curves
    """
    # Fillet Parameter Configuration
    if n == 1:
        crv_A = crv_B = curves[0]
        p, q = ease(crv_A)

    elif n == 2:
        crv_A, crv_B = curves
        ps, qs = ease(crv_A), ease(crv_B)
        p, q = closest(ps, qs)

    FILLET_OPTIONS["radius"] = radius

    # Fillet Execution
    fillet = CreateFilletCurves(crv_A, p, crv_B, q, **FILLET_OPTIONS)

    # Parameter Tracing
    if DEBUG:
        doc_objects.add_point(p)
        doc_objects.add_point(q)
        doc_objects.add_line(p, q)

    # Result Validation
    if not fillet:
        # Deselect inputs if failed with two curves
        if n == 2:
            doc_objects.deselect_all()
        info("Fillet Failed")

        raise FailSoft(FilletFailure)

    return fillet


def RunCommand(is_interactive):
    try:
        # Command Initialization
        curves, doc_curves, n = select_curves()  # FailSoft(InvalidSelection)
        radius = get_radius()

        # Fillet Execution
        fillet_success = perform_fillet(curves, n, radius)  # FailSoft(FilletFailure)

    # Failure Handling
    except FailSoft as e:
        type = e.args[0]
        error("Operation soft failed with {}".format(type))
        return SUCCESS

    # Cleanup
    doc_objects.delete_objects(doc_curves)

    # Finalization
    doc_objects.add_curves(fillet_success)

    return SUCCESS

if __name__ == "__main__":
    RunCommand(True)
