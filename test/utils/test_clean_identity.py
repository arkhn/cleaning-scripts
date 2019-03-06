from scripts import utils


def test_clean_identity():
    assert utils.clean_identity(None) == ""
    assert utils.clean_identity("NaN") == ""
    row_input = "Holà chicanos"
    assert utils.clean_identity(row_input) == row_input
