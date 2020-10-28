from scripts import utils
import datetime


def test_merge_concat_attached():

    # Tests string

    assert utils.merge_concat_attached("1") == "1"

    assert utils.merge_concat_attached("1", "2") == "12"

    assert utils.merge_concat_attached("1", "2", "3") == "123"

    assert utils.merge_concat_attached("a", "b", "ab") == "abab"

    assert utils.merge_concat_attached("a   ", " b", "  ab") == "a    b  ab"

    assert (
        utils.merge_concat_attached("Pyrog      ", " Is         ", "  Awesome ")
        == "Pyrog       Is           Awesome "
    )

    # Tests integer

    assert utils.merge_concat_attached(1, 2) == "12"

    assert utils.merge_concat_attached(1, 2, 3) == "123"

    # Tests datetime

    dateNow = datetime.datetime.now()
    assert utils.merge_concat_attached("a", dateNow) == "a" + str(dateNow)

    assert (
        utils.merge_concat_attached("testing", datetime.datetime(2020, 5, 17))
        == "testing2020-05-17 00:00:00"
    )

    # Test date

    assert utils.merge_concat_attached("testing", datetime.date(2020, 5, 17)) == "testing2020-05-17"

    # Test boolean

    assert utils.merge_concat_attached(True) == "True"

    assert utils.merge_concat_attached(True, False) == "TrueFalse"

    # Test mixed
    dateNow = datetime.datetime.now()
    assert (
        utils.merge_concat_attached("a", dateNow, datetime.date(2020, 5, 17), True)
        == "a" + str(dateNow) + "2020-05-17True"
    )
