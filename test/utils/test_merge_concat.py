from scripts import utils
import datetime


def test_merge_concat():

    # Tests string

    assert utils.merge_concat("1") == "1"

    assert utils.merge_concat("1", "2") == "1 2"

    assert utils.merge_concat("1", "2", "3") == "1 2 3"

    assert utils.merge_concat("a", "b", "ab") == "a b ab"

    # Tests integer

    assert utils.merge_concat(1, 2) == "1 2"

    assert utils.merge_concat(1, 2, 3) == "1 2 3"

    # Tests datetime

    dateNow = datetime.datetime.now()
    assert utils.merge_concat("a", dateNow) == "a " + str(dateNow)

    assert (
        utils.merge_concat("testing", datetime.datetime(2020, 5, 17))
        == "testing 2020-05-17 00:00:00"
    )
    # Tests date

    assert (
        utils.merge_concat("testing", datetime.date(2020, 5, 17))
        == "testing 2020-05-17"
    )

    # Tests boolean

    assert utils.merge_concat(True) == "True"

    assert utils.merge_concat(True, False) == "True False"
