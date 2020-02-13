def clean_osiris_UMLS(raw_input):
    if raw_input is None:
        return None
    return raw_input.replace("UMLS:", "")
