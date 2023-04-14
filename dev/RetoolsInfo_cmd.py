"""
Diagnostic information for the ReTools rhino plugin.

This command prints the python path to the rhino command line.
"""


import sys

from __plugin__ import title as plugin_name, version
import doctools
import geometry
import geometry.fit
import geometry.point
import geometry.sampler
import geometry.line


def RunCommand(is_interactive):
    """Print the python path."""
    print("Plugin: {}".format(plugin_name))
    print("Version: {}".format(version))
    print("")
    print("Python path for plugin:")

    for item in sys.path:
        print(item)

    return 0
