"""
This is a command template. It is used to create new commands.

{command details here}
"""

from command import SUCCESS, FAILURE
from services.log import info, error

from services.image_viewer import launch_imgs
from services.file import get_imgs_recursive
from services.rhino import current_folder

def RunCommand(is_interactive):
    try:
        workdir = current_folder()
    except:
        error("Failed to get current folder!")
        return FAILURE

    try:
        imgs = get_imgs_recursive(workdir)
    except:
        error("Failed to get images from work directory!")
        return FAILURE

    if not imgs:
        info("No images found in work directory!")
        return SUCCESS
    
    else:
        launch_imgs(imgs)
        return SUCCESS

