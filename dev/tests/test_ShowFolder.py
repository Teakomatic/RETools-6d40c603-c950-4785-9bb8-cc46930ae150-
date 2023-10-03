import subprocess
import time

import ShowFolder_cmd
from ShowFolder_cmd import OS


# Specialize test for current OS
if OS == "mac":
    REFERENCE_FOLDER = "/Applications"
    EXPLORER = "Finder"
    RUN_LIST = ["pgrep", "Finder"]
    KILL_LIST = ["killall", "Finder"]   

elif OS == "win":
    REFERENCE_FOLDER = "C:\\Windows"
    EXPLORER = "explorer.exe"
    RUN_LIST = ["tasklist", "/FI", "imagename eq explorer.exe"]
    KILL_LIST = ["taskkill", "/F", "/IM", "explorer.exe"]


def mock_current_folder():
    """Mock current_folder() to return a specific folder"""
    ShowFolder_cmd.current_folder = lambda: REFERENCE_FOLDER


def explorer_running(kill=False):
    """Check if explorer is running. Optionally kill it."""
    try:
        subprocess.check_call(RUN_LIST)
    except subprocess.CalledProcessError:
        return False
    else:
        if kill:
            print("Closing {}".format(EXPLORER))
            subprocess.call(KILL_LIST)


def test_ShowFolder():
    """Test the ShowFolder command on the current OS."""
    if explorer_running():
        print("Test ShowFolder: {} is running. Please close {} and try again.".format(EXPLORER, EXPLORER))
        return

    mock_current_folder(REFERENCE_FOLDER)

    ShowFolder_cmd.RunCommand(True)

    time.sleep(2)
    
    if not explorer_running(kill=True):
        print("Test ShowFolder: Failed. {} did not open.".format(EXPLORER))

    print("Test ShowFolder: Passed. {} opened.".format(EXPLORER))

   
if __name__ == "__main__":
    test_ShowFolder()