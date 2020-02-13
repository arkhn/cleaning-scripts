def clean_osiris_RECIST(raw_input):
    if raw_input is None:
        return None
    return raw_input.replace("RECIST:", "")
