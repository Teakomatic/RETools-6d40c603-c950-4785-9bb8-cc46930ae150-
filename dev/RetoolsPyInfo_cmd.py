"""
Diagnostic information for the ReTools rhino plugin.

This command prints the python path to the rhino command line.
"""

import sys

from __plugin__ import title as plugin_name, version

from command import SUCCESS
from services.log import info


def RunCommand(is_interactive):
    """Print Diagnostic Information for Retools."""

    # Plugin Name & Version
    info("Plugin: {}".format(plugin_name))
    info("Version: {}".format(version))
    info("")

    # Python Path
    info("Python path for plugin:")
    for item in sys.path:
        info(item)

    return SUCCESS
