"""
This command is part of the radius controller interface.

This command increases the radius.
"""

from services import log
from repo import radius_repo

def RunCommand(is_interactive):
    radius_repo.reset()
    log.info("Current radius is {}".format(radius_repo.get()))
    return 0
