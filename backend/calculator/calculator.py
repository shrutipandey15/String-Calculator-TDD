def add(numbers: str) -> int:
    """Return 0 for an empty string or the sum of the numbers."""
    if numbers == "":
        return 0
    num_list = map(int, numbers.split(","))
    return sum(num_list)
