from scripts.custom import clean_date


def test_clean_date():
    row_input = "2015-02-07T13:28:17"
    output = clean_date(row_input)
    assert output == "2015-02-07"
