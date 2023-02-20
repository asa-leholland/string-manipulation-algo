from main import transform_to_combination_array


def test_single_element_string():
    input_string = "schlaeger"
    expected_output = ["schlaeger"]

    output = transform_to_combination_array(input_string)

    assert output == expected_output


def test_multiple_element_string():
    input_string = "tischtennis schläger OR schlaeger"
    expected_output = ["tischtennis schläger", "tischtennis schlaeger"]

    output = transform_to_combination_array(input_string)

    assert output == expected_output

def test_multiple_ors():
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

def test_valid_or_condition():
    input_string = '"This"'
    output = transform_to_combination_array(input_string)
    assert output == []

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