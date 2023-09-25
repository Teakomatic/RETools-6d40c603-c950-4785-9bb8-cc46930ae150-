"""
This is a command template. It is used to create new commands.

{command details here}
"""

from command import SUCCESS, FAILURE
from services.log import info, error

from services import process
from services import file
from services import rhino


def RunCommand(is_interactive):
    try:
        workdir = rhino.current_folder()
    except:
        error("Failed to get current folder!")
        return FAILURE

    try:
        imgs = file.get_imgs_recursive(workdir)
    except:
        error("Failed to get images from work directory!")
        return FAILURE

    if not imgs:
        info("No images found in work directory!")
        return SUCCESS
    
    else:
        process.launch_imgs(imgs)
        return SUCCESS

