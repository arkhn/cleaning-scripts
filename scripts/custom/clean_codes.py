from scripts import utils
import re


terminologies = [
    "HL7:",
    "UMLS:",
    "LOINC:",
    "ATC:",
    "FINESS:",
    "MedDRA:",
    "CIM10:",
    "RECIST:",
    "OSIRIS:",
    "ICDO3:",
    "ICD-O-3:",
]


def clean_codes(raw_input):
    """Remove terminology system from code ("HL7:male") to ("male")
    """
    if utils.is_empty(raw_input):
        return None

    code = re.match(r"([A-z0-9]*:)(.*)", raw_input)

    if not code:
        return raw_input
    elif code.group(1) in terminologies:
        return code.group(2)
    else:
        return raw_input
