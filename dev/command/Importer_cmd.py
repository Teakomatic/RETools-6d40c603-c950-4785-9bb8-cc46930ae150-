"""
This is a command template. It is used to create new commands.

{command details here}
"""

from command import SUCCESS, FAILURE
from services.log import info, error


def RunCommand(is_interactive):
    info("Running command template")
    return SUCCESS


from import_tools import import_dxfs
from rhino import current_folder, no_redraw
from conf import IMPORT_BORDER

folder = current_folder()
print("Importing files from folder {}".format(folder))

with no_redraw():
    import_dxfs(folder, border=IMPORT_BORDER)
