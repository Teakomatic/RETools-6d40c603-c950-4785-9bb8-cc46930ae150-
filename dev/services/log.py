"""
/dev/services/log.py

This module provides a simple logging interface for the ReTools library.

Constraints:
- The logger accepts a single string.
- We have two log levels: debug (D) and info (I).
- Error messages are logged always.
"""

import functools
import System
import conf

def PRINT_SINK(msg):
    """Wrap the print statement into a function."""
    print(msg)

def FILE_SINK(msg):
    with open(conf.LOG_FILE, "a") as file:
        file.write(msg + "\n")

def DEFAULT_SINK(msg):
    FILE_SINK(msg)
    PRINT_SINK(msg)

# Main logging function
def log(msg, msg_level):
    """Log a message to the logger."""
    if  conf.LOG_LEVEL == "D" or msg_level != "D":
        formatted_msg = conf.LOG_MESSAGE_FORMAT.format(
            level=msg_level,
            timestamp=System.DateTime.Now.ToString(conf.TIMESTAMP_FORMAT),
            msg=msg
        )
        DEFAULT_SINK(formatted_msg)

# Interface functions
debug = functools.partial(log, msg_level="D")
info = functools.partial(log, msg_level="I")
error = functools.partial(log, msg_level="E")