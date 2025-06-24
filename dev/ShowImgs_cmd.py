"""
Show images from the currect job folder
"""

import subprocess
from services import log, conf, file

def RunCommand(is_interactive):
    imgs = file.get_files_recursive(
        file.current_folder(),
        conf.IMG_TYPES,
    )
    
    if not imgs:
        log.info("No images found in work directory!")
        return 0

    subprocess.Popen([conf.IMG_VIEWER] + imgs)
        
    return 0

