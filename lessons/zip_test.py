"""Test my zip function!"""
__author__ = "730403031"

from lessons.zip import zip


# Edge case for zip_test
def test_unequal_lists() -> None:
    """Testing two lists of unequal length."""
    idx: list[str] = ["Happy", "Tuesday", "Friends"]
    vals: list[int] = [1, 2]
    assert zip(idx, vals) == {}


# Use case 1 for zip_test
def test_equal_lists() -> None:
    """Testing a single input for an equal list of str and int."""
    idx: list[str] = ["Happy"]
    vals: list[int] = [1]
    assert zip(idx, vals) == {'Happy': 1}


# Use case 2 for zip_test
def test_equal_lists_greater_than_1() -> None:
    """Testing multiple inputs for an equal list of str and int."""
    idx: list[str] = ["Happy", "Birthday", "To", "You"]
    vals: list[int] = [1, 2, 3, 4]
    assert zip(idx, vals) == {'Happy': 1, 'Birthday': 2, 'To': 3, 'You': 4}