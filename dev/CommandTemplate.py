"""
This is a command template. It is used to create new commands.

{command details here}
"""

from command import SUCCESS, FAILURE
from services.log import info, error


def RunCommand(is_interactive):
    info("Running command template")
    return SUCCESS
