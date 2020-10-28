from scripts.custom import clean_dateTime


def test_clean_dateTime():
    # YYYY format test
    raw_input_1 = "2015"
    output_1 = clean_dateTime(raw_input_1)
    assert output_1 == "2015"

    # YYYY-MM format test
    raw_input_2 = "2015-02"
    output_2 = clean_dateTime(raw_input_2)
    assert output_2 == "2015-02"

    # YYYYMM format test
    raw_input_3 = "201502"
    output_3 = clean_dateTime(raw_input_3)
    assert output_3 == "2015-02"

    # YYYY-MM-DD format test
    raw_input_4 = "2015-02-07"
    output_4 = clean_dateTime(raw_input_4)
    assert output_4 == "2015-02-07"

    # YYYYMMDD format test
    raw_input_5 = "20150207"
    output_5 = clean_dateTime(raw_input_5)
    assert output_5 == "2015-02-07"

    # YYYY-MM-DD H:M:S format test
    raw_input_6 = "2015-02-07 13:28:17"
    output_6 = clean_dateTime(raw_input_6)
    assert output_6 == "2015-02-07T13:28:17+02:00"

    # YYYY-MM-DDTH:M:S format test
    raw_input_7 = "2015-02-07T13:28:17"
    output_7 = clean_dateTime(raw_input_7)
    assert output_7 == "2015-02-07T13:28:17+02:00"

    # YYYY-MM-DDTH:M:S+zz:zz format test
    raw_input_8 = "2015-02-07T13:28:17+05:00"
    output_8 = clean_dateTime(raw_input_8)
    assert output_8 == "2015-02-07T13:28:17+05:00"

    # YYYY-MM-DDTH:M:S-zz:zz format test
    raw_input_9 = "2015-02-07T13:28:17-05:00"
    output_9 = clean_dateTime(raw_input_9)
    assert output_9 == "2015-02-07T13:28:17-05:00"

    # RFC 1123 format test
    raw_input_10 = "Wed, 13 Mar 2075 00:00:00 GMT"
    output_10 = clean_dateTime(raw_input_10)
    assert output_10 == "2075-03-13T00:00:00+00:00"

    # YYYYMMDDHHMM format test
    raw_input_11 = "201502071740"
    output_11 = clean_dateTime(raw_input_11)
    assert output_11 == "2015-02-07T17:40:00+02:00"
