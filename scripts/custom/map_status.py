from enum import Enum

"""Map (0,1) code to (active, inactive) """


class activity(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    UNKNOWN = "unknown"


def map_status(raw_input):
    mapping = {"0": activity.ACTIVE.value, "1": activity.INACTIVE.value}
    if raw_input in mapping.keys():
        return mapping[raw_input]
    else:
        return activity.UNKNOWN.value
