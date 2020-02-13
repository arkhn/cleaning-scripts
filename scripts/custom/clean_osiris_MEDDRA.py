def clean_osiris_MEDDRA(raw_input):
    if raw_input is None:
        return None
    return raw_input.replace("MedDRA:", "")
