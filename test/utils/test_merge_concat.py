from scripts import utils


def test_merge_concat():
    assert utils.merge_concat("1") == "1"

    assert utils.merge_concat("1", "2") == "1 2"

    assert utils.merge_concat("1", "2", "3") == "1 2 3"

    assert utils.merge_concat("a", "b", "ab") == "a b ab"
