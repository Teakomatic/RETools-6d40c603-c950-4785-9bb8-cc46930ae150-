"""
This command will attemp to fillet the currently selected curve or pair of curves.

The command queries a repo for radius information. 

This command is intended to be used with a user facing radius controller interface.

In debug mode, we mark the starting points that we give to the native fillet command.

We fail soft for all errors, so that we do not interupt the repeat/* macro
"""


import command
from services import log, doc_objects
from geometry import closest, ease, fillet


def RunCommand(is_interactive):
    try:
        # Command Initialization
        curves, doc_curves, n = fillet.select_curves()
        radius = fillet.get_radius()

        # Fillet Execution
        fillet_success = fillet.perform_fillet(curves, n, radius)

    except command.FailSoft as e:
        # Fail gracefully to not interrup the `repeat FastFillet` command macro
        type = e.args[0]
        log.error("Operation soft failed with {}".format(type))
        return 0

    # Cleanup
    doc_objects.delete_objects(doc_curves)

    # Finalization
    [doc_objects.add_curve(fillet_segment) for fillet_segment in fillet_success]
    # Issue: add_curves throws "Cannot iterate polycurve", suggestign issue with lift function

    return 0