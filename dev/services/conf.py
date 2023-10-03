import rhinoscriptsyntax as rs

# Operating System: "mac" or "win"
OS = "win"

# Folders
BASE_FOLDER = rs.WorkingFolder()
SCANS_FOLDER = BASE_FOLDER + "\\Scans"
PICS_FOLDER = BASE_FOLDER + "\\Pics"

# Import Format
SHORT_ITEM_LENGTH = 36
TEXT_HEIGHT = 3
TEXT_HEIGHT_3D = 3
IMPORT_BORDER = 15
WORK_LAYER = "Final"

# Import Types
CAD_TYPES = ["dxf", "dwg"]
IMG_TYPES = ["jpg", "jpeg", "heic", "png", "gif"]

# Image Reviewer
WIN_IMG_VIEWER = "C:\Program Files\PureRef\PureRef.exe"

# Toolbars
TOOLBAR_RUI_PATH = "C:\Users\maxsu\OneDrive\Desktop\Max Work\Max Work\KyleTools\RhinoConfig\RE_toolbars.rui"
TOOLBAR_PLIST_PATH = None