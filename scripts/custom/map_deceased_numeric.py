from enum import Enum
"""Map deceased attribute from numeric code (0,1) to Boolean """

class Deceased(Enum):
    ALIVE = False
    DEAD = True
    UNKNOWN = None


def map_deceased(raw_input):
    mapping = {"1": Deceased.DEAD.value, "0": Deceased.ALIVE.value}
    if raw_input in mapping.keys():
        return mapping[raw_input]
    else:
        return Deceased.UNKNOWN.value