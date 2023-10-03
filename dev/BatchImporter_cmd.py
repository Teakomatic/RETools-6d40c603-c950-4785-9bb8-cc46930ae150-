"""
/RETools/dev/BatchImporter_cmd.py
(c) 2023 Mars Industrial (AGPLv3)

This script automates the process of importing DXF files into a Rhino .3dm file.

Usage:
This script is intended to be run from the command line, as part of a batch process:
>   {rhino.exe} -runscript="BatchImporter" {job_folder/job.3dm}

Effects:
- Import DXF files from the current directory into the open .3dm file.
- Log import success or failure.
- Save the .3dm file.
- Close Rhino.
"""


from services import info, error, FAILURE

from services.import_tools import import_dxfs
from services.rhino import current_folder, no_redraw, save, close


def RunCommand(is_interactive):
    folder = current_folder()
    info("Importing DXFs from {}".format(folder))

    try:
        with no_redraw():
            import_dxfs(folder, border=20)
            info("Import succeeded. Saving...")
            save()
            info("Save succeeded. Closing...")
            close()

    except Exception as e:
        error("Error encountered: {}".format(e))
        return FAILURE