"""Test that an empty string returns 0."""

from calculator.calculator import add
def test_empty_string():
    assert add("") == 0 