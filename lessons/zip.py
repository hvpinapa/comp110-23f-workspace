"""Combining two lists into a dictionary."""
__author__ = "730403031"


def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """Congregrating lists into a dictionary."""
    if len(keys) != len(values) or len(keys) == 0:
        return {}

    result = {}
    for idx in range(len(keys)):
        result[keys[idx]] = values[idx]
    return result