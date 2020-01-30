from enum import Enum
from scripts import ScriptError

"""Map (0,1) code to (active, inactive) """


class activity(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    UNKNOWN = "unknown"


def map_status(raw_input):
    mapping = {"0": activity.ACTIVE.value, "1": activity.INACTIVE.value}
    try:
        return mapping[raw_input]
    except KeyError:
        raise ScriptError(
            f"could not map status {raw_input} (must be in {', '.join(mapping.keys())})"
        )
