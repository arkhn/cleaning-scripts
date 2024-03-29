from scripts import custom


def test_map_priority():

    raw_input_1 = "0"
    output_1 = custom.map_priority(raw_input_1)
    assert output_1 == "stat"

    raw_input_2 = 0
    output_2 = custom.map_priority(raw_input_2)
    assert output_2 == "stat"

    raw_input_3 = "1"
    output_3 = custom.map_priority(raw_input_3)
    assert output_3 == "asap"

    raw_input_4 = 1
    output_4 = custom.map_priority(raw_input_4)
    assert output_4 == "asap"

    raw_input_5 = "2"
    output_5 = custom.map_priority(raw_input_5)
    assert output_5 == "urgent"

    raw_input_6 = 2
    output_6 = custom.map_priority(raw_input_6)
    assert output_6 == "urgent"

    raw_input_7 = "50"
    output_7 = custom.map_priority(raw_input_7)
    assert output_7 == "routine"

    raw_input_8 = 50
    output_8 = custom.map_priority(raw_input_8)
    assert output_8 == "routine"

    raw_input_9 = "-1"
    output_9 = custom.map_priority(raw_input_9)
    assert output_9 == "routine"

    raw_input_10 = -1
    output_10 = custom.map_priority(raw_input_10)
    assert output_10 == "routine"
