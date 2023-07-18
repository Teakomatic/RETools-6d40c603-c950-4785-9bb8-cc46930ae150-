from inspect import stack, getmodule

DEBUG = 0
INFO = 1

NAMES = {DEBUG: "DEBUG", INFO: "INFO"}

LEVEL = INFO

import os

def clean_path(path):
    """
    Split prefix from a rhpython plugin code path.

    C:\Users\maxsu\AppData\Roaming\McNeel\Rhinoceros\7.0\Plug-ins\PythonPlugins\RETools (6d40c603-c950-4785-9bb8-cc46930ae150)\dev\log\__init__.py
    => log\__init__.py
    """
    directories, filename = os.path.split(path)
    dev_index = directories.index('dev')
    local_path = os.path.join(directories[dev_index:] + filename)
    return local_path



def format_msgs(level, msgs):
    """
    Use inspect module to extract file, function, and line info for calling context

    Ref: https://docs.python.org/2.7/library/inspect.html#module-inspect
    """

    # Get executing context
    frame = stack()[2]
    file = clean_path(frame[1])
    function = frame[3]
    line = str(frame[2])

    # Format message string
    header = "[{}] {}.L{}::{}: ".format(
        NAMES[level],
        file,
        line,
        function,
    )

    # Convert numbers to strings for python 2.7 join
    msgs = [str(msg) for msg in msgs]
    msgs = " ".join(msgs)

    message_string = "{}  {}".format(header, msgs)

    return message_string


def info(*msgs):
    """
    Log basic operating messages
    """
    if LEVEL > INFO:
        return
    message_string = format_msgs(INFO, msgs)
    print(message_string)


def debug(*msgs):
    if LEVEL > DEBUG:
        return
    message_string = format_msgs(DEBUG, msgs)
    print(message_string)


if __name__ == "__main__":
    info("testing", "123")
    debug("testing", "123")
