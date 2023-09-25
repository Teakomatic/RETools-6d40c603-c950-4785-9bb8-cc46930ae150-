import notify
import rhinoscriptsyntax as rs

# Folders
BASE_FOLDER = rs.WorkingFolder()
SCANS_FOLDER = BASE_FOLDER + "\\Scans"
PICS_FOLDER = BASE_FOLDER + "\\Pics"

# Import Format
TEXT_HEIGHT = 3
TEXT_HEIGHT_3D = 3
IMPORT_BORDER = 15
WORK_LAYER = "Final"

# Import Types
CAD_TYPES = ["dxf", "dwg"]
IMG_TYPES = ["jpg", "jpeg", "heic", "png", "gif"]

# Image Reviewer
PURE_REF = "C:\Program Files\PureRef\PureRef.exe"
