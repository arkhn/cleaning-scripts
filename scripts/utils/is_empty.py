def is_empty(value):
    """(Logic) is None, NaN, empty or blank str"""
    return (
        value is None
        or value == "NaN"
        or value == ""
        or value in "                        "
    )
