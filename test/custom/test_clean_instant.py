from scripts.custom.clean_instant import clean_instant


def test_clean_instant():
    # YYYY-MM-DD H:M:S format test
    raw_input_1 = "2015-02-07 13:28:17"
    output_1 = clean_instant(raw_input_1)
    print(output_1)
    assert output_1 == "2015-02-07T13:28:17+02:00"

    # YYYY-MM-DDTH:M:S format test
    raw_input_2 = "2015-02-07T13:28:17"
    output_2 = clean_instant(raw_input_2)
    print(output_2)
    assert output_2 == "2015-02-07T13:28:17+02:00"

    ### RFC 1123 format test
    raw_input_3 = "Wed, 13 Mar 2075 00:00:00 GMT"
    output_3 = clean_instant(raw_input_3)
    print(output_3)
    assert output_3 == "2075-03-13T00:00:00+02:00"
