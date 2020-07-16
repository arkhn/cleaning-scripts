from scripts import utils


def to_empty(raw_input):
    """Return None when entry is -1
    """
    if utils.is_empty(raw_input) or raw_input == "-1":
        return None
    else:
        return raw_input