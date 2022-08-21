"""
    localities general rates
"""

from .. import cls
from .. import general_classes
from .. import special_classes
from .. import county_classes

from ..utilities import InputHelper
from ..utilities import InputTesters
from ..utilities import LogicalWork
from ..utilities import Printer

from .mecklenburg import main as mecklenburg
from .union import main as union
from .stanly import main as stanly
# from .cabarrus import main as cabarrus
from .iredell import main as iredell
# from .rowan import main as rowan
from .gaston import main as gaston
# from .lancaster import main as lancaster
# from .york import main as york

def load_all_counties(which_run):
    """
    load_all_counties Initalizes all counties or reinitalizeses based on argument

    Args:
        which_run (str): inital or reload based on desired effect
    """

    if which_run == "inital":
        pass
    elif which_run == "reload":
        general_classes.Counties.reset_counties()

    general_classes.Counties.add_county(mecklenburg())
    general_classes.Counties.add_county(union())
    general_classes.Counties.add_county(stanly())
    # general_classes.Counties.add_county(cabarrus())
    general_classes.Counties.add_county(iredell())
    # general_classes.Counties.add_county(rowan())
    general_classes.Counties.add_county(gaston())
    # general_classes.Counties.add_county(lancaster())
    # general_classes.Counties.add_county(york())
