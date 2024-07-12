"""
dev/BatchImporter_cmd.py
(c) 2023 Mars Industrial (AGPLv3)

This script automates the process of importing DXF files into a Rhino .3dm file.

Usage:
This script is intended to be run from rhino by the user in Rhino.

Effects:
- Imports DXF files from the current job directory into the open .3dm file.
- Logs import success or failure to the console and to a log file.

"""


from services import info, error, FAILURE, SUCCESS

from services.import_tools import import_dxfs
from services.rhino import current_folder, no_redraw


def RunCommand(is_interactive):
    folder = current_folder()
    info("Importing DXFs from {}".format(folder))

    try:
        with no_redraw():
            import_dxfs(folder, border=20)
            info("Import succeeded.")
            return SUCCESS

    except Exception as e:
        error("Error encountered: {}".format(e))
        return FAILURE