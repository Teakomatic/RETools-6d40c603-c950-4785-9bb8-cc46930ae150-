"""
This is a command template. It is used to create new commands.

{command details here}
"""


from services import info, error, debug, SUCCESS, FAILURE
from services.conf import OS
from services.rhino import current_folder
from services.process import spawn
from services.my_string import singe_quote

MAC_EXPLORER = "open"
WIN_EXPLORER = "explorer"
FILE_EXPLORER = MAC_EXPLORER if OS == "mac" else WIN_EXPLORER


def RunCommand(is_interactive):
    workdir = current_folder()
    quoted_workdir = singe_quote(workdir)
    info("Opening file explorer at {}".format(workdir))

    spawn([
        FILE_EXPLORER,
        quoted_workdir,
    ])

    return SUCCESS
