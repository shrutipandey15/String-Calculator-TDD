import re

def add(numbers: str) -> int:
    """Return sum of numbers, supporting custom delimiters and handling negative numbers."""
    if not numbers:
        return 0
    
    delimiter = ",|\n"

    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split("\n", 1)

    num_list = list(map(int, re.split(delimiter, numbers)))
    
    negatives = [num for num in num_list if num < 0]
    if negatives:
        raise ValueError(f"Negatives numbers not allowed: {', '.join(map(str, negatives))}")
    return sum(num_list)
