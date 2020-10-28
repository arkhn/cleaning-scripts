from scripts import get_script


def test_get_script_unauthorized():
    # unauthorized function
    func = "my_fancy_function"
    try:
        _ = get_script(func)
        assert False
    except NameError:
        pass


def test_get_script_custom():
    # custom function
    row_input = "20191103"
    func = "clean_date"
    assert get_script(func)(row_input) == "2019-11-03"


def test_get_script_utils():
    # utility function
    row_input = " my text  "
    func = "make_title"
    assert get_script(func)(row_input) == "My Text"


def test_get_script_logic():
    # logical function
    func = 'if_valid(strip, "Hello")'

    row_input = ""
    assert get_script(func)(row_input) == ""

    row_input = "holà"
    assert get_script(func)(row_input) == "Hello"

    row_input = "NaN"
    assert get_script(func)(row_input) == ""

    func = "if_valid(strip, 'Hello')"
    row_input = "holà"
    assert get_script(func)(row_input) == "Hello"

    func = 'if_valid(strip, "7")'
    row_input = "holà"
    assert get_script(func)(row_input) == "7"

    func = 'if_valid(strip, "9.2")'
    row_input = "holà"
    assert get_script(func)(row_input) == "9.2"

    func = "if_valid(strip, make_title)"

    row_input = ""
    assert get_script(func)(row_input) == ""

    row_input = "  holà"
    assert get_script(func)(row_input) == "Holà"

    # Un authorized param
    func = "if_valid(strip, my_fancy_function)"
    try:
        _ = get_script(func)
        assert False
    except ValueError:
        pass
