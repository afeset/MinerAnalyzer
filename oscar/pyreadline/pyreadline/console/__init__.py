import glob,sys

success = False
in_ironpython = "IronPython" in sys.version

if in_ironpython:
    try:
        from ironpython_console import *
        success = True
    except ImportError:
        raise
elif sys.platform.startswith('linux'):
    try:
        from ansi_console import *
        success = True
    except ImportError, x:
        raise
else:
    try:
        from console import *
        success = True
    except ImportError:
        pass
        raise

if not success:
    raise ImportError(
            "Could not find a console implementation for your platform")
