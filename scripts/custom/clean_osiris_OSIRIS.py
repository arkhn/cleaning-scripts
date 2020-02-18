def clean_osiris_OSIRIS(raw_input):
    if raw_input is None:
        return None
    return raw_input.replace("OSIRIS:", "")
