from enum import Enum
import logging
from scripts import utils


class MaritalStatus(Enum):
    Divorced = "D"
    Annulled = "A"
    Interlocutory = "I"
    LegallySeparated = "L"
    Married = "M"
    Polygamous = "P"
    NeverMarried = "S"
    DomesticPartner = "T"
    unmarried = "U"
    Widowed = "W"
    unknown = "UNK"


def map_marital_status(code):
    """Map marital status for mimic database
    """
    status = MaritalStatus
    mapping = {
        "MARRIED": status.Married.value,
        "SINGLE": status.unmarried.value,
        "WIDOWED": status.Widowed.value,
        "SEPARATED": status.LegallySeparated.value,
        "DIVORCED": status.Divorced.value,
        "UNKNOWN": status.unknown.value,
    }
    if code in mapping.keys():
        return mapping[code]
    elif utils.is_empty(code):
        return status.unknown.value
    else:
        logging.warning("In {}, args {} not recognised".format("marital_status", code))
        return code
