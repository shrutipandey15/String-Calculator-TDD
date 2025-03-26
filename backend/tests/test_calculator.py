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
    try:
        add("1,-2,3,-4")
    except ValueError as e:
        assert str(e) == "Negatives numbers not allowed: -2, -4"
    else:
        assert False, "Exception not raised"

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