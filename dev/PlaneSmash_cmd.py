from services import doc_objects, log
import command
import geometry

def RunCommand(is_interactive):
    """
    Command to correct the inclincation defect of selected geometry
    """

    # Fetch selected items
    selection = doc_objects.get_selected()

    # Succeed on empty selection
    # This lets us use the command in "repeat" macros
    if not selection:
        log.info("No items selected. Doing nothing.")
        return 0

    # Report selection
    log.info(
        "selected {} curves and {} points".format(
            len(selection.curves), len(selection.points)
        )
    )

    # Correct items
    correction = geometry.flatten(selection)
    selection.transform(correction)
