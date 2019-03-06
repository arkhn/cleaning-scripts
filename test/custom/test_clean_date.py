from scripts.custom import clean_date


def test_clean_date():
    row_input = "20191103"
    output = clean_date(row_input)
    assert output == "2019-11-03T00:00:00"
