from scripts import utils
import re


terminologies = ["HL7:", "UMLS:", "LOINC:", "ATC:"]


def clean_codes(raw_input):
    """
        Remove all chars before and including the first colon (example: "HL7:male" --> "male" )
    """
    if utils.is_empty(raw_input):
        return None

    code = re.match(r"([A-z0-9]*:)(.*)", raw_input)

    if not code:
        return None
    elif code.group(1) in terminologies:
        return code.group(2)
