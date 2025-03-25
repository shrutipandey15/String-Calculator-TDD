import re
def add(numbers: str) -> int:
    """Return sum of numbers, supporting comma and newline as delimiters."""
    if numbers == "":
        return 0
    num_list = map(int, re.split(r",|\n", numbers))
    return sum(num_list)
