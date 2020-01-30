from enum import Enum
from scripts import ScriptError


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    UNKNOWN = "unknown"


def map_gender_numeric(raw_input):
    """Map gender from numeric code (1,2) to FHIR standard """
    mapping = {"1": Gender.MALE.value, "2": Gender.FEMALE.value}
    try:
        return mapping[raw_input]
    except KeyError:
        raise ScriptError(
            f"could not map numeric gender {raw_input} (must be in {', '.join(mapping.keys())})"
        )
