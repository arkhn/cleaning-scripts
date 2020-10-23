from scripts.custom import clean_comparatedNumber

def test_clean_comparatedNumber():
  
    # XX
    raw_input_1 = "31"
    output_1 = clean_comparatedNumber(raw_input_1)
    assert output_1 == "31"

    # X.X
    raw_input_2 = "0.32"
    output_2 = clean_comparatedNumber(raw_input_2)
    assert output_2 == "0.32"

    # <=XX
    raw_input_3 = "<=33"
    output_3 = clean_comparatedNumber(raw_input_3)
    assert output_3 == "33"

    # >=XX
    raw_input_4 = ">=34"
    output_4 = clean_comparatedNumber(raw_input_4)
    assert output_4 == "34"

    # =XX
    raw_input_5 = "=35"
    output_5 = clean_comparatedNumber(raw_input_5)
    assert output_5 == "35"

    # =>XX
    raw_input_6 = "=>36"
    output_6 = clean_comparatedNumber(raw_input_6)
    assert output_6 == "36"

    # =<XX
    raw_input_7 = "=<37"
    output_7 = clean_comparatedNumber(raw_input_7)
    assert output_7 == "37"

    # <XX
    raw_input_8 = "<38"
    output_8 = clean_comparatedNumber(raw_input_8)
    assert output_8 == "38"

    # >XX
    raw_input_9 = ">39"
    output_9 = clean_comparatedNumber(raw_input_9)
    assert output_9 == "39"

test_clean_comparatedNumber()