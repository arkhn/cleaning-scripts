from scripts import utils


def test_clean_identity():
    assert utils.strip(None) == ""
    assert utils.strip("NaN") == ""
    row_input = "Holà chicanos"
    assert utils.strip(row_input) == row_input
