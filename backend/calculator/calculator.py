import re

def add(numbers: str) -> int:
    """Return sum of numbers, supporting comma, newline, and custom delimiters."""
    if not numbers:
        return 0
    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split("\n", 1)
        num_list = map(int, re.split(fr"{re.escape(delimiter)}|\n", numbers))
    else:
        num_list = map(int, re.split(r",|\n", numbers))
    return sum(num_list)
