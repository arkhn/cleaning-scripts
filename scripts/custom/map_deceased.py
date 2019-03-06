from enum import Enum


class Deceased(Enum):
    ALIVE = False
    DEAD = True
    UNKNOWN = None


def map_deceased(raw_input):
    mapping = {"O": Deceased.DEAD.value, "N": Deceased.ALIVE.value}
    if raw_input in mapping.keys():
        return mapping[raw_input]
    else:
        return Deceased.UNKNOWN.value
