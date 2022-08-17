"""
    localities general rates
"""

from .. import cls
from .. import general_classes

from ..utilities import InputHelper
from ..utilities import InputTesters
from ..utilities import LogicalWork
from ..utilities import Printer

from .. import special_classes

from .mecklenburg import main as mecklenburg
from .union import main as union

from .iredell import main as iredell
# from .cabarrus import main as cabarrus
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
    # classes.Counties.add_county(stanly())
    # classes.Counties.add_county(cabarrus())
    general_classes.Counties.add_county(iredell())
    # classes.Counties.add_county(rowan())
    general_classes.Counties.add_county(gaston())
    # classes.Counties.add_county(lancaster())
    # classes.Counties.add_county(york())
