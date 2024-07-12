"""
Diagnostic information for the ReTools rhino plugin.

This command prints the python path to the rhino command line.
"""

import os
import sys

from __plugin__ import title as plugin_name, version

from command import SUCCESS
from services.log import info

SCRIPT_PATH = os.path.abspath(__file__)
COMMAND_DIRECTORY = os.path.dirname(SCRIPT_PATH)
COMMAND_FILES = [f for f in os.listdir(COMMAND_DIRECTORY) if f.endswith('_cmd.py')]
COMMAND_NAMES = [f[:-7] for f in COMMAND_FILES]

def RunCommand(is_interactive):
    """Print Diagnostic Information for Retools."""
    info("Retools Python Diagnostic Information")
    info("Plugin: {}".format(plugin_name))
    info("Version: {}".format(version))
    info("")

    info("Commands:")
    for number, command in enumerate(COMMAND_NAMES, start=1):
        info("{number}: {command}".format(number=number, command=command))
    info("")

    info("Python path:")
    for number, item in enumerate(sys.path, start=1):
        info("{number}: {item}".format(number=number, item=item))

    return SUCCESS
