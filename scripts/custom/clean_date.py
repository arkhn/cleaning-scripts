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
    try:
        date = datetime.datetime.strptime(raw_input, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        pass

    if date:
        iso_date = date.strftime("%Y-%m-%d")
        return iso_date
    else:
        return raw_input
