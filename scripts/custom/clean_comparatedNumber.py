from scripts import utils
import re 

comparator = [
    "<=",
    ">=",
    "=",
    "=>",
    "=<",
    ">",
    "<",
    "",
]

def clean_comparatedNumber(raw_input):
    """Remove the comparator sign from a comparated number ("=>16") to ("16")
    """

    if utils.is_empty(raw_input):
        return None
    
    comparatedNumber=re.match(r"([<=>]?[=<>=]?)(.*)",raw_input)

    if not comparatedNumber:
        # print ('1: '+raw_input)
        """To know in which case we are"""
        return raw_input
    elif comparatedNumber.group(1) in comparator:
        # print ('2: '+comparatedNumber.group(2))
        """To know in which case we are"""
        return comparatedNumber.group(2)
