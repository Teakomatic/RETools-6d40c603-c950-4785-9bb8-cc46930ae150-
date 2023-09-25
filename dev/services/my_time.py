import System

# The timestamp format is a .NET datetime format string.
TIMESTAMP_FORMAT = "yyyy.MM.dd H:mm:ss.fff"


def timestamp():
    """Return a timestamp string."""
    return System.DateTime.Now.ToString(TIMESTAMP_FORMAT)

