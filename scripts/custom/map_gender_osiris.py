from enum import Enum


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    UNKNOWN = "unknown"


def map_gender_osiris(raw_input):
    mapping = {"HL7:M": Gender.MALE.value, "HL7:F": Gender.FEMALE.value}
    if raw_input in mapping.keys():
        return mapping[raw_input]
    else:
        return Gender.UNKNOWN.value
