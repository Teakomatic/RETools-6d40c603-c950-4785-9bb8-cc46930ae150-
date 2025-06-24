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

from services import log, rhino, import_tools

def RunCommand(is_interactive):
    folder = file.current_folder()
    log.info("Importing DXFs from {}".format(folder))

    try:
        with rhino.no_redraw():
            import_tools.import_dxfs(folder, border=20)
            log.info("Import succeeded. Saving...")
            rhino.save()
            log.info("Save succeeded. Closing...")
            rhino.close()
        return 0

    except Exception as e:
        error("Error encountered: {}".format(e))
        return 1