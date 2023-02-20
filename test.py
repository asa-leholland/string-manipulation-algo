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