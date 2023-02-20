from main import transform_to_combination_array


def test_should_return_single_element_string_input_as_output():
    input_string = "schlaeger"
    expected_output = ["schlaeger"]

    output = transform_to_combination_array(input_string)

    assert output == expected_output


def test_should_return_multiple_element_string_with_single_or_as_unique_combinations():
    input_string = "tischtennis schläger OR schlaeger"
    expected_output = ["tischtennis schläger", "tischtennis schlaeger"]

    output = transform_to_combination_array(input_string)

    assert output == expected_output


def test_should_return_multiple_element_string_with_multiple_ors_as_unique_combinations():
    input_string = "tt OR tischtennis OR tischtenis schläger OR schlaeger"
    expected_output = [
        "tt schläger",
        "tt schlaeger",
        "tischtennis schläger",
        "tischtennis schlaeger",
        "tischtenis schläger",
        "tischtenis schlaeger",
    ]

    output = transform_to_combination_array(input_string)

    assert output == expected_output


def test_should_return_input_with_double_quote_character_and_one_or_as_empty_list():
    input_string = '"This test OR fail'
    output = transform_to_combination_array(input_string)
    assert output == []


def test_should_return_input_with_double_quote_character_and_one_or_as_input():
    input_string = '"This test fail'
    output = transform_to_combination_array(input_string)
    assert output == ['"This test fail']


def test_multiple_ors_and_multiple_elements():
    input_string = "a OR b c z d OR e f OR g OR h OR i"
    expected_output = [
        "a c z d f",
        "a c z d g",
        "a c z d h",
        "a c z d i",
        "a c z e f",
        "a c z e g",
        "a c z e h",
        "a c z e i",
        "b c z d f",
        "b c z d g",
        "b c z d h",
        "b c z d i",
        "b c z e f",
        "b c z e g",
        "b c z e h",
        "b c z e i"
    ]

    output = transform_to_combination_array(input_string)

    assert output == expected_output


def test_ten_or_conditions():
    input_string = "a OR b 1 a OR b 2 a OR b 3 a OR b 4 a OR b 5 a OR b 6 a OR b 7 a OR b 8 a OR b 9 a OR b 10"
    output = transform_to_combination_array(input_string)
    assert len(output) == 1024
    assert output[0] == "a 1 a 2 a 3 a 4 a 5 a 6 a 7 a 8 a 9 a 10"
    assert output[1] == "a 1 a 2 a 3 a 4 a 5 a 6 a 7 a 8 a 9 b 10"
    assert len(output) == len(set(output))
