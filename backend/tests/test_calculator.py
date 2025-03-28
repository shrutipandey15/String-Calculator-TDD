import pytest
from calculator.calculator import add
def test_empty_string():
    """Test that an empty string returns 0."""
    assert add("") == 0 

def test_single_number():
    """Test that a single number returns itself."""
    assert add("1") == 1
    assert add("2") == 2

def test_two_numbers():
    """Test that two numbers are added."""
    assert add("1,2") == 3 
    assert add("3,4") == 7

def test_multiple_numbers():
    """Test that multiple numbers are added."""
    assert add("1,2,3") == 6
    assert add("5,10,15,20") == 50

def test_newline_as_delimiter():
    """Test that newline are treated as delimiters like commas."""
    assert add("1\n2,3") == 6
    assert add("5\n10\n15,20") == 50

def test_custom_delimiter():
    """Test that a custom delimiter can be used."""
    assert add("//;\n1;2") == 3
    assert add("//:\n5:10:15:20") == 50

def test_negative_numbers():
    """Test that negative numbers raise an exception with the list of negative numbers."""
    with pytest.raises(ValueError, match="Negative numbers not allowed: -2, -4"):
        add("1,-2,3,-4")

def test_multi_character_delimiter():
    """Test that multi-character delimiters are supported."""
    assert add("//***\n1***2***3") == 6
    assert add("//[xyz]\n5xyz10xyz15") == 30

def test_multiple_custom_delimiters():
    """Test that multiple custom delimiters are supported at once."""
    assert add("//[*][%]\n1*2%3") == 6
    assert add("//[;][###]\n5###10;15") == 30

def test_ignore_numbers_over_1000():
    """Test that numbers greater than 1000 are ignored."""
    assert add("2,1001,6") == 8
    assert add("1000,1001,1") == 1001
    assert add("1001,1001,1001") == 0
    assert add("1000,1001,1002") == 1000

def test_special_characters_delimiters():
    """Test delimiters with special regex characters."""
    assert add("//[.][*]\n1.2*3") == 6
    assert add("//[+][?]\n1+2?3") == 6

def test_consecutive_delimiters():
    """Test consecutive delimiters."""
    with pytest.raises(ValueError, match="Invalid input: Consecutive delimiters"):
        add("1,,2")
    with pytest.raises(ValueError, match="Invalid input: Consecutive delimiters"):
        add("1,,2,3")

def test_non_integer_input():
    """Test handling of non-integer inputs."""
    with pytest.raises(ValueError, match="Invalid input: Non-integer values"):
        add("1,2,three")
    with pytest.raises(ValueError, match="Invalid input: Non-integer values"):
        add("1,2,3.5,4")

def test_whitespace_handling():
    """Test handling of whitespace."""
    assert add(" 1, 2 , 3 ") == 6
    assert add("1, 2,  3") == 6
    assert add("1000  , 1 ") == 1001

def test_only_delimiters():
    """Test input with only delimiters should raise an error."""
    with pytest.raises(ValueError,match="Invalid input: Only delimiters"):
        add(",,")
