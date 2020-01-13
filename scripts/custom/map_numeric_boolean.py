def map_numeric_boolean(raw_input):
    """Map attribute from numeric code (0,1) to Boolean """
    mapping = {"1": True, "0": False}
    if raw_input in mapping.keys():
        return mapping[raw_input]
    else:
        return None
