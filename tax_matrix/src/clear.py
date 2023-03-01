"""
    only contains the great and powerful clear function
"""

from . import os


def cls():
    """
    Clears the command outline on the screen.

    This function uses the `os` module to run the `cls` command on Windows systems
    or the `clear` command on non-Windows systems.

    Example:
        cls()
    """
    os.system("cls" if os.name == "nt" else "clear")
    # use "cls()" to clear screen
