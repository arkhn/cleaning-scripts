import datetime
from scripts import utils


def clean_instant(raw_input):  # noqa: C901
    if not isinstance(raw_input, str):
        raw_input = str(raw_input)
    if utils.is_empty(raw_input):
        return ""

    date = None

    formats = [
        "%Y",
        "%Y-%m",
        "%Y%m",
        "%Y-%m-%d",
        "%Y%m%d",
        "%Y%m%d%H%M",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
    ]
    for fmt in formats:
        try:
            date = datetime.datetime.strptime(raw_input, fmt)
            result = date.strftime("%Y-%m-%dT%H:%M:%S+02:00")

        except ValueError:
            pass

    # Handle YYYY-MM-DDTH:M:S+zz:zz
    try:
        date = datetime.datetime.strptime(raw_input, "%Y-%m-%dT%H:%M:%S+%z")
        result = date.strftime("%Y-%m-%dT%H:%M:%S%z")
    except ValueError:
        pass

    # Handle YYYY-MM-DDTH:M:S-zz:zz
    try:
        date = datetime.datetime.strptime(raw_input, "%Y-%m-%dT%H:%M:%S-%z")
        result = date.strftime("%Y-%m-%dT%H:%M:%S%z")
    except ValueError:
        pass

    # Handle RFC 1123 format
    try:
        date = datetime.datetime.strptime(raw_input, "%a, %d %b %Y %H:%M:%S GMT")
        result = date.strftime("%Y-%m-%dT%H:%M:%S+00:00")
    except ValueError:
        pass

    if date is None:
        return raw_input

    return result
