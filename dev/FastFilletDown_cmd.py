"""
This command is part of the radius controller interface.

This command increases the radius.
"""

from command import SUCCESS
from repo import radius_repo


def RunCommand(is_interactive):
    print("Current radius is {}".format(radius_repo.get()))

    print("Decreasing radius")
    radius_repo.down()

    print("New radius is {}".format(radius_repo.get()))

    return SUCCESS
