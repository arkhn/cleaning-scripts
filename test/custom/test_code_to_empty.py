from scripts import custom


def test_code_to_empty():
    assert custom.code_to_empty("-1") is None
    assert custom.code_to_empty("(sans)") is None
    assert custom.code_to_empty("-2") is not None
