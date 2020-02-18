def clean_osiris_LOINC(raw_input):
    if raw_input is None:
        return None
    return raw_input.replace("LOINC:", "")
