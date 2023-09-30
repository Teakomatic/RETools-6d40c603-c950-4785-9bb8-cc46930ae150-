"""
/RETools/dev/LoadRETools_cmd.py
(c) 2023 Mars Industrial (AGPLv2)

Bootstrap the RETools plugin.

Deals with the fact that the toolbar is a plist on Mac and a rui on Windows.

Effects:
- Load the RETools toolbar.
"""

from __plugin__ import version
from services.log import info, debug
from services.conf import OS
from services.conf import TOOLBAR_PLIST_PATH
from services.conf import TOOLBAR_RUI_PATH

if OS == "Mac":
    from RhinoMac.Runtime import MacPlatformService

else:
    from Rhino.RhinoApp import ToolbarFiles


def RunCommand(is_interactive):
    if OS == "Mac":
        debug("Loading RETools toolbar from {}".format(TOOLBAR_PLIST_PATH))
        MacPlatformService.LoadToolPaletteCollection(TOOLBAR_PLIST_PATH)

    else:
        debug("Loading RETools toolbar from {}".format(TOOLBAR_RUI_PATH))
        ToolbarFiles.Open(TOOLBAR_RUI_PATH)

    info("Loaded ReTools Version {}.".format(version))
