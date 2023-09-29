"""
/RETools/dev/LoadRETools_cmd.py

Bootstrap the RETools plugin.
"""

from Rhino.RhinoApp import ToolbarFiles

from __plugin__ import version
from services.log import info, debug
from services.conf import TOOLBAR_FILE_PATH


def RunCommand(is_interactive):
    if not ToolbarFiles.FindByPath(TOOLBAR_FILE_PATH):
        debug("Loading RETools toolbar from {}".format(TOOLBAR_FILE_PATH))
        ToolbarFiles.Open(TOOLBAR_FILE_PATH)
    
    info("ReTools Version {} was loaded.".format(version))
