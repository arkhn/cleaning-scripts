from enum import Enum
from scripts import utils


class Authorization(Enum):
    PERMIT = "permit"
    DENY = "deny"


def map_genetic_permission_osiris(raw_input):
    if utils.is_empty(raw_input):
        return None
    mapping = {
        "UMLS:C1298907": Authorization.PERMIT.value,
        "UMLS:C1298908": Authorization.DENY.value,
    }
    if raw_input in mapping.keys():
        return mapping[raw_input]
