import re

def add(numbers: str) -> int:
    """
    Returns the sum of numbers in a given string, supporting custom delimiters of any length 
    and handling edge cases such as negative numbers and non-integer values.

    The function follows these rules:
    - An empty string returns 0.
    - The default delimiters are commas (`,`) and newlines (`\n`).
    - Custom delimiters can be defined at the beginning of the string using the `//[delimiter]\n` format.
      - Multiple custom delimiters are allowed, enclosed in square brackets (e.g., `//[*][%]\n1*2%3`).
    - Numbers greater than 1000 are ignored.
    - If only delimiters are present (e.g., `",,"`), an exception is raised.
    - Consecutive delimiters (e.g., `"1,,2"`) are not allowed.
    - If a negative number is encountered, an exception is raised, listing all negative numbers in the input.

    Args:
        numbers (str): The input string containing numbers separated by delimiters.

    Returns:
        int: The sum of valid numbers, ignoring those greater than 1000.

    Raises:
        ValueError: If the input contains only delimiters, consecutive delimiters, non-integer values, 
                    or negative numbers (listing them in the error message).
    """

    if not numbers:
        return 0
    
    delimiter = ",|\n"

    if numbers.startswith("//"):
        parts = numbers[2:].split("\n", 1)
        if len(parts) < 2 or not parts[0]:
            raise ValueError("Invalid delimiter format")
        
        custom_delimiter, numbers = numbers[2:].split("\n", 1)

        match = re.findall(r"\[(.*?)\]", custom_delimiter)
        delimiter = "|".join(map(re.escape, match)) if match else re.escape(custom_delimiter)

    if re.fullmatch(fr"({delimiter})+", numbers):
        raise ValueError("Invalid input: Only delimiters")

    if re.search(fr"({delimiter}){{2,}}", numbers):
        raise ValueError("Invalid input: Consecutive delimiters")
    
    try:
        num_list = list(map(int, re.split(delimiter, numbers)))
    except ValueError:
        raise ValueError("Invalid input: Non-integer values")
    
    negatives = [n for n in num_list if n < 0]
    if negatives:
        raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

    return sum(num for num in num_list if num <= 1000)
