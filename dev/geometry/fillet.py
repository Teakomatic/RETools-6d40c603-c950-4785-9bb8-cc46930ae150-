from Rhino.Geometry.Curve import CreateFilletCurves
from scriptcontext import doc
from services import doc_objects, log
import command
import geometry
from repo import radius_repo

FILLET_OPTIONS = {
    "join": True,
    "trim": True,
    "arcExtension": True,
    "tolerance": doc.ModelAbsoluteTolerance,
    "angleTolerance": doc.ModelAngleToleranceDegrees,
}

DEBUG_FILLETS = False


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
        p, q = geometry.ease(crv_A)

    elif n == 2:
        crv_A, crv_B = curves
        # Get 10% near end points
        ps, qs = geometry.ease(crv_A), geometry.ease(crv_B)
        # Get closest pair of ends
        p, q = geometry.closest(ps, qs)

    FILLET_OPTIONS["radius"] = radius

    # Fillet Execution
    fillet = CreateFilletCurves(crv_A, p, crv_B, q, **FILLET_OPTIONS)

    # Parameter Tracing
    if DEBUG_FILLETS:
        doc_objects.add_point(p)
        doc_objects.add_point(q)
        doc_objects.add_line(p, q)

    # Result Validation
    if not fillet:
        # Deselect inputs if failed with two curves
        if n == 2:
            doc_objects.deselect_all()
        log.info("Fillet Failed")

        raise command.FailSoft(FilletFailure)

    return fillet


class FilletFailure(Exception):
    """
    Signals:
    - Self fillet failed
        - The curve is a line
        - The curve is closed
        - The ends are colinear
    - Two curve fillet failed
        - The fillet radius is too large
        - The fillet starting points diverge
    """

    pass


class InvalidSelection(Exception):
    """
    Exception for invalid selection

    This means:
    - No objects selected
    - More than two objects selected
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
        log.info("Please select one or two curves. {} selected.".format(n))

        # Deselect if 3+ objects selected
        if n > 2:
            doc_objects.deselect_all()

        # n = 1: Keep object selected in case self fillet fails
        # This allows user to select a second object on next attempt

        raise command.FailSoft(InvalidSelection)

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
            log.info("Enter the radius of the circle.")
            radius_input = input("Radius: ")
            log.debug("radius_input type: {}".format(type(radius_input)))

            # Input Conversion
            if type(radius_input) in {float, int}:
                radius = radius_input

            elif isinstance(radius_input, str):
                radius = float(radius_input.strip())

        # Input Validation
        except ValueError:
            log.error("Invalid input. Please enter a valid number.")
            continue

        except Exception as e:
            log.error("Input Error: {}. Using default radius".format(e))
            log.debug("Error type: {}".format(type(e)))
            radius = 0

        if radius < 0:
            log.error("Radius must be a positive number or zero.")
            continue

        break

    # Repository Radius Fetch (if applicable)
    if radius == 0:
        radius = radius_repo.get()

    log.info("Current radius: {}".format(radius))
    return radius
