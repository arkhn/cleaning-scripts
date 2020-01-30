from scripts import ScriptError


def make_title(raw_input):
    """Capitalize and strip"""
    if not isinstance(raw_input, str):
        raise ScriptError(f"{raw_input} must be a string")
    return raw_input.title().strip()
