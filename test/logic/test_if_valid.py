from scripts.logic import if_valid
from scripts.utils import strip, make_title


def test_if_logic():

    my_script = if_valid(strip, "Hello")

    row_input = ""
    assert my_script(row_input) == ""

    row_input = "holà"
    assert my_script(row_input) == "Hello"

    row_input = "NaN"
    assert my_script(row_input) == ""

    my_script = if_valid(strip, make_title)

    row_input = ""
    assert my_script(row_input) == ""

    row_input = "  holà"
    assert my_script(row_input) == "Holà"
