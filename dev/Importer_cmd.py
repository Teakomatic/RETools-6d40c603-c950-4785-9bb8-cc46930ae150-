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

from services import file, log, import_tools, rhino

def RunCommand(is_interactive):
    
    folder = file.current_folder()

    try:
        with rhino.no_redraw():
            log.info("Importing DXFs from {}".format(folder))
            import_tools.import_dxfs(folder, border=20)
            log.info("Import succeeded.")
            return 0

    except Exception as e:
        log.error("Error encountered: {}".format(e))
        return 1