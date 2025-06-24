"""
Diagnostic information for the ReTools rhino plugin.

This command prints the python path to the rhino command line.
"""

import os
import sys

import __plugin__
from services import log

def RunCommand(is_interactive):
    SCRIPT_PATH = os.path.abspath(__file__)
    COMMAND_DIRECTORY = os.path.dirname(SCRIPT_PATH)
    COMMAND_FILES = [f for f in os.listdir(COMMAND_DIRECTORY) if f.endswith('_cmd.py')]
    COMMAND_NAMES = [f[:-7] for f in COMMAND_FILES]

    """Print Diagnostic Information for Retools."""
    log.info("Retools Python Diagnostic Information")
    log.info("Plugin: {}".format(__plugin__.title))
    log.info("Version: {}".format(__plugin__.version))
    log.info("")

    log.info("Commands:")
    for number, command in enumerate(COMMAND_NAMES, start=1):
        log.info("{number}: {command}".format(number=number, command=command))
    log.info("")

    log.info("Python path:")
    for number, item in enumerate(sys.path, start=1):
        log.info("{number}: {item}".format(number=number, item=item))

    return 0
