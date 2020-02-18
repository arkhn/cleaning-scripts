from scripts import utils
import re


def clean_quantity(raw_input):
    """Removes that input is conform to FHIR quantity type
    """

    if utils.is_empty(raw_input):
        return ""
    number = re.search(r"-?(0|[1-9][0-9]*)(\.[0-9]+)?([eE][+-]?[0-9]+)?", raw_input)
    if not number or number.group(0) != raw_input:
        return ""
    else:
        return raw_input
