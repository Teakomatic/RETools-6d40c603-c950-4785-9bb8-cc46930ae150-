import System

# The timestamp format is a .NET datetime format string.
DEFAULT_TIMESTAMP_FORMAT = "yy.MM.dd H:mm:ss.fff"


def timestamp(timestamp_format=None):
    """Return a timestamp string."""
    timestamp_format = timestamp_format or DEFAULT_TIMESTAMP_FORMAT
    return System.DateTime.Now.ToString(timestamp_format)

