from scripts import utils

# function clean_osiris_codes
# remove all chars before and including the first colon


def clean_osiris_codes(raw_input):
    if utils.is_empty(raw_input):
        return None
    firstColonIndex = raw_input.find(":") + 1
    return raw_input[firstColonIndex:]
