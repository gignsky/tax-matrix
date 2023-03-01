"""
    only contains the great and powerful clear function
"""

from . import os


def cls():
    """
    cls will clear command outline
    """
    os.system("cls" if os.name == "nt" else "clear")
    # use "cls()" to clear screen
