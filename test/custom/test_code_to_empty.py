from scripts import custom

def test_codes_to_empty():
    assert custom.code_to_empty("-1") == None
    assert custom.code_to_empty("(sans)") == None
    assert custom.code_to_empty("-2") != None
    