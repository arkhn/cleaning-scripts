from scripts import ScriptError
from scripts.utils import is_empty


def strip(raw_input):
    """Strip strings, convert NaN and None to empty string"""
    if not isinstance(raw_input, str):
        raise ScriptError(f"{raw_input} must be a string")

    if is_empty(raw_input):
        return ""

    return raw_input.strip()
