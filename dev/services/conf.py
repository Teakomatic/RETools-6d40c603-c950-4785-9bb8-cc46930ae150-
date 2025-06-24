import rhinoscriptsyntax as rs

# Operating System: "mac" or "win"
OS = "win"

# Logging
LOG_FILE = r"\\VBOXSVR\logs\REToolsPy.log"
LOG_LEVEL = "D"
DEBUG = True
LOG_MESSAGE_FORMAT = "{timestamp}({level}) {msg}"
# DotNet timestamp format
TIMESTAMP_FORMAT = "yy.MM.dd H:mm:ss.fff"

# Folders
BASE_FOLDER = rs.WorkingFolder()
SCANS_FOLDER = BASE_FOLDER + r"\Scans"
PICS_FOLDER = BASE_FOLDER + r"\Pics"

# Import Format
SHORT_ITEM_LENGTH = 36
TEXT_HEIGHT = 3
TEXT_HEIGHT_3D = 3
IMPORT_BORDER = 15
WORK_LAYER = "Final"

# Import Types
CAD_TYPES = ["dxf", "dwg"]
IMG_TYPES = ["jpg", "jpeg", "heic", "png", "gif"]

# Viewers
if OS == "win":
    FILE_EXPLORER = "explorer"
    IMG_VIEWER = "C:\Program Files\PureRef\PureRef.exe"

else:
    FILE_EXPLORER = "open"
    IMG_VIEWER = "open"

# Toolbars
TOOLBAR_RUI_PATH = "\\VBOXSVR\setup\REtoolbar.rui"
TOOLBAR_PLIST_PATH = None