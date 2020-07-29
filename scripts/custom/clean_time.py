import datetime

import re
from scripts import utils


def clean_time(raw_input):  # noqa: C901
    if not isinstance(raw_input, str):
        raw_input = str(raw_input)
    if utils.is_empty(raw_input):
        return ""
    time = None

    # HH:MM:SS
    try:
        time = datetime.datetime.strptime(raw_input, "%H:%M:%S").time()
    except ValueError:
        pass

    # HH:MM:SS.f
    try:
        time = datetime.datetime.strptime(raw_input, "%H:%M:%S.%f").time()
    except ValueError:
        pass

    # Handle YYYYMMDDHHMMSS
    try:
        time = datetime.datetime.strptime(raw_input, "%Y%m%d%H%M%S").time()
    except ValueError:
        pass

    # Handle YYYYMMDDHHMM
    try:
        time = datetime.datetime.strptime(raw_input, "%Y%m%d%H%M").time()
    except ValueError:
        pass

    # Handle YYYY-MM-DD H:M:S
    try:
        time = datetime.datetime.strptime(raw_input, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        pass

    # Handle YYYY-MM-DDTH:M:S
    try:
        time = datetime.datetime.strptime(raw_input, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        pass

    # Handle YYYY-MM-DDTH:M:S+zzzz
    try:
        time = datetime.datetime.strptime(raw_input, "%Y-%m-%dT%H:%M:%S%z")
    except ValueError:
        pass

    # Handle RFC 1123 format
    try:
        time = datetime.datetime.strptime(raw_input, "%a, %d %b %Y %H:%M:%S %Z")
    except ValueError:
        pass

    # Handle H:M:S+zz:zz
    try:
        time = datetime.datetime.strptime(raw_input, "%H:%M:%S%z").time()
    except ValueError:
        pass

    # Handle HH::MM::SS
    try:
        time = datetime.datetime.strptime(raw_input, "%H::%M::%S").time()
    except ValueError:
        pass

    # Handle HH MM SS
    try:
        time = datetime.datetime.strptime(raw_input, "%H %M %S").time()
    except ValueError:
        pass

    # Handle HHMMSS
    try:
        time = datetime.datetime.strptime(raw_input, "%H%M%S").time()
    except ValueError:
        pass

    # Handle HHMM
    try:
        time = datetime.datetime.strptime(raw_input, "%H%M").time()
    except ValueError:
        pass

    if not time:
        time = datetime.datetime.strptime("00:00:00", "%H:%M:%S").time()

    return time.strftime("%H:%M:%S")
