"""
/import/lib/log.py

This module provides a simple logging interface for the ReTools library.
"""

from functools import partial
from os.path import abspath
import System

from my_time import timestamp

# The log format can contain the following placeholders: {level}, {timestamp}, {msg}
FORMAT = "{level} {timestamp}: {msg}"

LOG_FILE = abspath("../logs/import.log")

# Log sinks
def FILE_LOGGER(msg):
    open(LOG_FILE, "a").write(msg + "\n")
def PRINT_LOGGER(msg):
    print(msg)
def CONSOLE_LOGGER(msg):
    System.Console.WriteLine
DEFAULT_LOGGER = PRINT_LOGGER

# Level may be  INFO or DEBUG
LEVEL = "INFO"

# Main logging function
def log(msg, level, format=FORMAT):
    """Log a message to the logger."""
    if level == "DEBUG" and LEVEL != "DEBUG":
        return
    formatted_msg = format.format(
        level=level,
        timestamp=timestamp(),
        msg=msg
    )
    DEFAULT_LOGGER(formatted_msg)

# Interface functions
info = partial(log, level="INFO")
error = partial(log, level="ERROR")
debug = partial(log, level="DEBUG")

# Test
if __name__ == "__main__":
    info("This is an info message.")
    error("This is an error message.")

    DEFAULT_LOGGER = FILE_LOGGER
    info("This is an info message with a file logger.")