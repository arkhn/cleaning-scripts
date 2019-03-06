from enum import Enum


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    UNKNOWN = "unknown"


def map_gender(raw_input):
    mapping = {"M": Gender.MALE.value, "F": Gender.FEMALE.value}
    if raw_input in mapping.keys():
        return mapping[raw_input]
    else:
        return Gender.UNKNOWN.value
