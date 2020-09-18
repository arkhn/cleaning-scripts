from scripts.custom import clean_hour


def test_clean_hour():

    # YYYY
    raw_input_1 = "800"
    output_1 = clean_hour(raw_input_1)
    assert output_1 == "08:00"

    # YYYY-MM
    raw_input_2 = "2015"
    output_2 = clean_hour(raw_input_2)
    assert output_2 == "20:15"

    # YYYYMM
    raw_input_3 = "0"
    output_3 = clean_hour(raw_input_3)
    assert output_3 == "00:00"

    # YYYY-MM-DD
    raw_input_4 = "00"
    output_4 = clean_hour(raw_input_4)
    assert output_4 == "00:00"

    # YYYYMMDD
    raw_input_5 = "000"
    output_5 = clean_hour(raw_input_5)
    assert output_5 == "00:00"

    # YYYY-MM-DD H:M:S
    raw_input_6 = "1700"
    output_6 = clean_hour(raw_input_6)
    assert output_6 == "17:00"
