from calculator.calculator import add
def test_empty_string():
    """Test that an empty string returns 0."""
    assert add("") == 0 

def test_single_number():
    """Test that a single number returns itself."""
    assert add("1") == 1
    assert add("2") == 2