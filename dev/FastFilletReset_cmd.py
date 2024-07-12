"""
This command is part of the radius controller interface.

This command increases the radius.
"""

from command import SUCCESS
from services.log import info
from repo import radius_repo


def RunCommand(is_interactive):
    radius_repo.reset()
    info("Current radius is {}".format(radius_repo.get()))
    return SUCCESS
