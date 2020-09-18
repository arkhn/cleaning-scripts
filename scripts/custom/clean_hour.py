from scripts import utils


def clean_hour(raw_input):
    """Convert 800, 1400, 1715 to 08:00, 14:00, 17.15
    """
    if not isinstance(raw_input, str):
        raw_input = str(raw_input)
    if utils.is_empty(raw_input):
        return ""

    hour = raw_input
    while len(hour) < 4:
        hour = "0" + hour

    hour = hour[:2] + ":" + hour[2:]

    return hour
