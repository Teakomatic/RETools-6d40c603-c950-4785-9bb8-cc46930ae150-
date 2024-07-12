from process import spawn
from conf import OS, WIN_IMG_VIEWER, MAC_IMG_VIEWER

if OS == "win":
    VIEWER_LIST = [WIN_IMG_VIEWER]

elif OS == "mac":
    VIEWER_LIST = ["open", "-a", MAC_IMG_VIEWER]


def launch_imgs(imgs):
    if OS == "win":
        spawn(VIEWER_LIST + imgs)

    elif OS == "mac":
        pass