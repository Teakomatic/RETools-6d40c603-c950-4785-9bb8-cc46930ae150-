"""
This command is part of the radius controller interface.

This command increases the radius.
"""

from services import log
from repo import radius_repo


def RunCommand(is_interactive):
    log.info("Current radius is {}".format(radius_repo.get()))

    log.info("Decreasing radius")
    radius_repo.down()

    log.info("New radius is {}".format(radius_repo.get()))

    return 0
