import datetime

from scripts import utils


def clean_date(raw_input):  # noqa: C901
    if not isinstance(raw_input, str):
        raw_input = str(raw_input)
    if utils.is_empty(raw_input):
        return ""

    date = None

    # Handle YYYY-MM-DD
    try:
        date = datetime.datetime.strptime(raw_input, "%Y-%m-%d")
    except ValueError:
        pass

    # Handle YYYYMMDD
    try:
        date = datetime.datetime.strptime(raw_input, "%Y%m%d")
    except ValueError:
        pass

    # Handle YYYY-MM-DD H:M:S
    try:
        date = datetime.datetime.strptime(raw_input, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        pass

    # Handle YYYY-MM-DDTH:M:S
    try:
        date = datetime.datetime.strptime(raw_input, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        pass

    # Handle RFC 1123 format
    try:
        date = datetime.datetime.strptime(raw_input, "%a, %d %b %Y %H:%M:%S GMT")
    except ValueError:
        pass

    if date is None:
        return raw_input

    return date.strftime("%Y-%m-%d")
