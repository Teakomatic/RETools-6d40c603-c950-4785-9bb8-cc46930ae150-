"""
This is a command template. It is used to create new commands.

{command details here}
"""

from command import SUCCESS, FAILURE
from services.log import info, error


def RunCommand(is_interactive):
    info("Running command template")
    return SUCCESS


"""
app/batch_importer.py; (c) 2023 Mars Industrial.

This script automates the process of importing DXF files into a Rhino .3dm file.

To invoke this script from the Rhino CLI use the following command:
> {rhino.exe} -runscript="import.app.batch_importer" {job_folder/job.3dm}
"""

import import_tools
import rhino

import log
from log import info, error, FILE_LOGGER

log.LOGGER = FILE_LOGGER("batch_importer.log")

def batch_import_dxfs_from_folder():
    """
    Import all DXF files from the current job directory into the open .3dm file.
        
    After importing, save, and close Rhino.

    Effects:
        - Imports DXF files from the current job directory into the open .3dm file.
        - Logs import success or failure to the console and to a log file.
        - Saves the .3dm file.
        - Closes Rhino.
    """

    folder = rhino.current_folder()
    info("Importing DXFs from {}".format(folder))

    try:
        with rhino.no_redraw():
            import_tools.import_dxfs(folder, border=20)
            info("Import succeeded. Saving...")
            rhino.save()

    except Exception as e:
        error("Error encountered: {}".format(e))

    finally:
        rhino.close()

if __name__ == "__main__":
    batch_import_dxfs_from_folder()