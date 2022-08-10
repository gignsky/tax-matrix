"""
    YOU FOUND THE SOURCE MODUDULE's init file
"""

import os
import debugpy

from . import config
from . import utilities
from . import classes
from . import special_county_classes
from . import localities

def cls():
    """
    cls will clear command outline
    """
    os.system("cls" if os.name == "nt" else "clear")
    # use "cls()" to clear screen
