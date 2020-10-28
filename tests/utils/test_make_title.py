from scripts import utils


def test_make_title():
    row_input = " my text  "
    output = utils.make_title(row_input)
    assert output == "My Text"
