from enum import Enum
"""Map gender from numeric code (1,2) to FHIR standard """

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    UNKNOWN = "unknown"


def map_gender(raw_input):
    mapping = {"1": Gender.MALE.value, "2": Gender.FEMALE.value}
    if raw_input in mapping.keys():
        return mapping[raw_input]
    else:
        return Gender.UNKNOWN.value
