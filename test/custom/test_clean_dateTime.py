from scripts.custom.clean_dateTime import clean_dateTime


def test_clean_dateTime():
    raw_input_1 = "2015"
    output_1 = clean_dateTime(raw_input_1)
    print(output_1)
    assert output_1 == "2015"

    raw_input_2 = "2015-02"
    output_2 = clean_dateTime(raw_input_2)
    print(output_2)
    assert output_2 == "2015-02"

    raw_input_3 = "2015-02-07"
    output_3 = clean_dateTime(raw_input_3)
    print(output_3)
    assert output_3 == "2015-02-07"

    raw_input_4 = "2015-02-07 13:28:17"
    output_4 = clean_dateTime(raw_input_4)
    print(output_4)
    assert output_4 == "2015-02-07T13:28:17+01:00"

    raw_input_5 = "2015-02-07T13:28:17"
    output_5 = clean_dateTime(raw_input_5)
    print(output_5)
    assert output_5 == "2015-02-07T13:28:17+01:00"

    raw_input_6 = "2015-02-07T13:28:17+05:00"
    output_6 = clean_dateTime(raw_input_6)
    print(output_6)
    assert output_6 == "2015-02-07T13:28:17+05:00"

    raw_input_7 = "2015-02-07T13:28:17-05:00"
    output_7 = clean_dateTime(raw_input_7)
    print(output_7)
    assert output_7 == "2015-02-07T13:28:17-05:00"


test_clean_dateTime()
