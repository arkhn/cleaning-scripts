import datetime
from scripts import utils


def clean_instant(raw_input):  # noqa: C901
    if not isinstance(raw_input, str):
        raw_input = str(raw_input)
    if utils.is_empty(raw_input):
        return ""

    date = None

    # Handle YYYY
    try:
        date = datetime.datetime.strptime(raw_input, "%Y")
        result = date.strftime("%Y-%m-%dT%H:%M:%S+02:00")

    except ValueError:
        pass

    # Handle YYYY-MM
    try:
        date = datetime.datetime.strptime(raw_input, "%Y-%m")
        result = date.strftime("%Y-%m-%dT%H:%M:%S+02:00")
    except ValueError:
        pass

    # Handle YYYYMM
    try:
        date = datetime.datetime.strptime(raw_input, "%Y%m")
        result = date.strftime("%Y-%m-%dT%H:%M:%S+02:00")
    except ValueError:
        pass

    # Handle YYYY-MM-DD
    try:
        date = datetime.datetime.strptime(raw_input, "%Y-%m-%d")
        result = date.strftime("%Y-%m-%dT%H:%M:%S+02:00")
    except ValueError:
        pass

    # Handle YYYYMMDD
    try:
        date = datetime.datetime.strptime(raw_input, "%Y%m%d")
        result = date.strftime("%Y-%m-%dT%H:%M:%S+02:00")
    except ValueError:
        pass

    # Handle YYYY-MM-DD H:M:S
    try:
        date = datetime.datetime.strptime(raw_input, "%Y-%m-%d %H:%M:%S")
        result = date.strftime("%Y-%m-%dT%H:%M:%S+02:00")
    except ValueError:
        pass

    # Handle YYYY-MM-DDTH:M:S
    try:
        date = datetime.datetime.strptime(raw_input, "%Y-%m-%dT%H:%M:%S")
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
