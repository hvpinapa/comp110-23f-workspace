"""Summing the elements of a list using different loops."""
__author__ = "730403031"


def w_sum(vals: list[float]) -> float:
    """Returns float sum using a while loop."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum = sum + vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Returns float sum using for loop."""
    sum: float = 0.0
    idx: int = 0
    for nums in vals:
        sum = sum + vals[idx]
        idx += 1
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Returns float sum using a for loop and range function."""
    sum: float = 0.0
    idx: int = 0
    for nums in range(0, len(vals)):
        sum += vals[idx]
        idx += 1
    return sum