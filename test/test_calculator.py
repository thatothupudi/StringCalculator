from string_calculator.calculator import add
import pytest

def test_empty_string():
    assert add("") == 0

def test_add_one_number():
    assert add("12") == 12

def test_add_two_numbers():
    assert add("8,7") == 15

def test_add_many_numbers():
    assert add("1,4,3,4,7") == 19

def test_new_lines():
    assert add("1\n2,3") == 6

def test_different_delimiters():
    assert add("//;\n1;2") == 3

def test_negative_numbers():
    with pytest.raises(Exception) as err:
        assert add("//;\n-1;2,-3")
        assert str(err.value) == "Negative numbers are not allowed: "

def test_more_than_twenty():
    assert add("//;\n1;2,21") == 24

def test_delimeter_len():
    assert add("//[***]\n1***2***3") == 6

def test_multiple_delimeters():
    assert add("//[*][%]\n1*2%3") == 6


def test_add_deli_and_many():
    assert add("1,2,7,//[*],9[%]") == 19
    

    
    