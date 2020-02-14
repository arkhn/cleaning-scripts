from scripts import utils
import re


# function clean_osiris_codes
# remove all chars before and including the first colon

# OSIRIS database has other codes that are not accepted by FHIR : ["OSIRIS:",]

osirisCodes = ["HL7:", "UMLS:", "LOINC:", "ATC:"]


def clean_osiris_codes(raw_input):
    if utils.is_empty(raw_input):
        return None

    code = re.search("[A-z0-9]*:", raw_input).group(0)
    if code in osirisCodes:
        firstColonIndex = raw_input.find(":") + 1
        return raw_input[firstColonIndex:]
