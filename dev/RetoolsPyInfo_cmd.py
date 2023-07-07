"""
Diagnostic information for the ReTools rhino plugin.

This command prints the python path to the rhino command line.
"""

import sys

from __plugin__ import title as plugin_name, version

from command import SUCCESS


def RunCommand(is_interactive):
    """Print Diagnostic Information for Retools."""

    # Plugin Name & Version
    print("Plugin: {}".format(plugin_name))
    print("Version: {}".format(version))
    print("")

    # Python Path
    print("Python path for plugin:")
    for item in sys.path:
        print(item)

    return SUCCESS
