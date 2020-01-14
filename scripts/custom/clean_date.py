import datetime

from scripts import utils


def clean_date(raw_input):
    if not isinstance(raw_input, str):
        raw_input = str(raw_input)
    if utils.is_empty(raw_input):
        return ""

    # Handle YYYYMMDD
    try:
        date = datetime.datetime.strptime(raw_input, "%Y-%m-%d %H:%M:%S")
        iso_date = date.strftime("%Y-%m-%d")
        return iso_date
    except ValueError:
        return raw_input

