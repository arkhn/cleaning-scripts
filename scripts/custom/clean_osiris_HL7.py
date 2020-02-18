def clean_osiris_HL7(raw_input):
    if raw_input is None:
        return None
    return raw_input.replace("HL7:", "")
