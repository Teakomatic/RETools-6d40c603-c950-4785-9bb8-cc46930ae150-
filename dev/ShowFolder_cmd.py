"""
Open the current job folder in the file explorer
"""

import subprocess
from services import conf, log, file

def RunCommand(is_interactive):
    workdir = file.current_folder()
    log.info("Opening {}".format(workdir))

    subprocess.Popen([
        conf.FILE_EXPLORER,
        workdir,
    ])

    return 0
