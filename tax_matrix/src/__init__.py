"""
    YOU FOUND THE SOURCE MODUDULE
"""
import os


def cls():
    os.system("cls" if os.name == "nt" else "clear")
    # use "cls()" to clear screen


from .config import *
from . import localities
from . import utilities
