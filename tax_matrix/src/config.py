"""
General CONFIGURATION information
"""


def CURRENT_VERSION():
    var = "2.0.0"
    return var


def DATE_REVISED():
    var = "08.05.2022"
    return var


def DESCRIPTION():
    var = f"Revised as of: {DATE_REVISED()} | Statement Generator for CLT-Surrounding Tax Districts"
    return var


def LONG_DESCRIPTION():
    var = f"Revised as of: {DATE_REVISED()} | A tax matrix calculator for form-filling purposes that will generate a statement estimating taxes for a property based on it's specified tax rates"
    return var


def DEPENDENCIES():
    var = ["art", "colorama"]
    return var
