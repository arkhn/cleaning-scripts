import datetime

from scripts import utils


def clean_date(raw_input):
    if not isinstance(raw_input, str):
        raw_input = str(raw_input)
    if utils.is_empty(raw_input):
        return ""

    date = None

    # Handle YYYYMMDD
    try:
        date = datetime.datetime.strptime(raw_input, "%Y%m%d")
    except ValueError:
        pass

    # Handle YYYY-MM-DD H:M:S
    if date is None:
        try:
            date = datetime.datetime.strptime(raw_input, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            pass

    # Handle YYYY-MM-DDTH:M:S
    if date is None:
        try:
            date = datetime.datetime.strptime(raw_input, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            pass

    if date is not None:
        return date.strftime("%Y-%m-%d")
    else:
        return raw_input
