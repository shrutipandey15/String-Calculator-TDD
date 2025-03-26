import re

def add(numbers: str) -> int:
    """Return sum of numbers, supporting custom delimiters of any length and handling negative numbers."""
    if not numbers:
        return 0
    
    delimiter = ",|\n"

    if numbers.startswith("//"):
        custom_delimiter, numbers = numbers[2:].split("\n", 1)

        match = re.findall(r"\[(.*?)\]", custom_delimiter)
        if match:
            delimiter = "|".join(map(re.escape, match))
        else:
            delimiter = re.escape(custom_delimiter)

    num_list = list(map(int, re.split(delimiter, numbers)))

    negatives = [num for num in num_list if num < 0]
    if negatives:
        raise ValueError(f"Negatives numbers not allowed: {', '.join(map(str, negatives))}")
    
    #ignore numbers greater than 1000
    return sum(num for num in num_list if num <= 1000)
