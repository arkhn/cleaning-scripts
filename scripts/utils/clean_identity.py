def clean_identity(raw_input):
    if raw_input is None or raw_input == "NaN":
        return ""
    return raw_input.strip()
