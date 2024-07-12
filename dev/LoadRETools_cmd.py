"""
/RETools/dev/LoadRETools_cmd.py
(c) 2023 Mars Industrial (AGPLv2)

Bootstrap the RETools plugin.

Effects:
- Loads the RETools toolbar.
- Reports the RETools version.
"""

import os

from __plugin__ import version
from services.log import info, debug, error
from services.conf import OS
from services.conf import TOOLBAR_PLIST_PATH
from services.conf import TOOLBAR_RUI_PATH

if OS == "mac":
    from RhinoMac.Runtime import MacPlatformService

    TOOLBAR_PATH = TOOLBAR_PLIST_PATH
    is_toolbar_loaded = MacPlatformService.IsToolPaletteCollectionOpen
    load_toolbar = MacPlatformService.LoadToolPaletteCollection

else:
    from Rhino.RhinoApp import ToolbarFiles
    
    TOOLBAR_PATH = TOOLBAR_RUI_PATH
    is_toolbar_loaded = ToolbarFiles.FindByPath
    load_toolbar = ToolbarFiles.Open
    
def RunCommand(is_interactive):
    if os.path.exists(TOOLBAR_PATH):
        if not is_toolbar_loaded(TOOLBAR_PATH):
            debug("Loading RETools toolbar from {}".format(TOOLBAR_PATH))
            load_toolbar(TOOLBAR_PATH)
    else:
        error("RETools toolbar not found at {}. Skipping.".format(TOOLBAR_PATH))

    info("Loaded RETools Version {}.".format(version))