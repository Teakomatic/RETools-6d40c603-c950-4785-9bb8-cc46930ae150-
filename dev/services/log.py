"""
/dev/services/log.py

This module provides a simple logging interface for the ReTools library.

Constraints:
- The logger accepts a single string.
- We have two log levels: debug (D) and info (I).
- Error messages are logged always.
"""

from functools import partial
from os.path import abspath
import System

import my_time

LOG_FILE = "X:\REToolsPy.log"
LOG_LEVEL = "D"
LOG_MESSAGE_FORMAT = "{timestamp}({level}) {msg}"
TIMESTAMP_FORMAT = "yy.MM.dd H:mm:ss.fff"

# Utility functions
def tee(f, g):
    """Return a function that applies f and g to its argument."""
    def h(x):
        return f(x), g(x)
    return h

def print_fn(msg):
    """Wrap the print statement into a function."""
    print(msg)


def FILE_SINK(msg):
    with open(LOG_FILE, "a") as file:
        file.write(msg + "\n")
PRINT_SINK = print_fn
FILE_PRINT_SINK = tee(FILE_SINK, PRINT_SINK)
CONSOLE_SINK = System.Console.WriteLine
DEFAULT_SINK = FILE_PRINT_SINK

# Main logging function
def log(msg, msg_level):
    """Log a message to the logger."""
    if  LOG_LEVEL == "D" or msg_level != "D":
        formatted_msg = LOG_MESSAGE_FORMAT.format(
            level=msg_level,
            timestamp=my_time.timestamp(TIMESTAMP_FORMAT),
            msg=msg
        )
        DEFAULT_SINK(formatted_msg)


# Interface functions
debug = partial(log, msg_level="D")
info = partial(log, msg_level="I")
error = partial(log, msg_level="E")


# Test
if __name__ == "__main__":
    info("Log file: {}".format(LOG_FILE))
    info("Log level: {}".format(LOG_LEVEL))
    info("Timestamp format: {}".format(TIMESTAMP_FORMAT))
    debug("This is a debug message.")
    info("This is an info message.")
    error("This is an error message.")