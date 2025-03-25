def add(numbers: str) -> int:
    """Return 0 for an empty string or the number itself for a single number."""
    if numbers == "":
        return 0
    return int(numbers)