from scripts import utils


def test_merge_concat_attached():
    assert utils.merge_concat_attached("1") == "1"

    assert utils.merge_concat_attached("1", "2") == "12"

    assert utils.merge_concat_attached("1", "2", "3") == "123"

    assert utils.merge_concat_attached("a", "b", "ab") == "abab"

    assert utils.merge_concat_attached("a   ", " b", "  ab") == "a    b  ab"

    assert (
        utils.merge_concat_attached("Pyrog      ", " Is         ", "  Awesome ")
        == "Pyrog       Is           Awesome "
    )
