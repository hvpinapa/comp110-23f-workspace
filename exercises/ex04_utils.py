"""EX04 - List Utils!"""
__author__ = "730403031"


def all(input_list: list[int], match: int) -> bool:
    input_idx: int = 0
    while input_idx < len(input_list):
        if input_list[input_idx] != match:
            return False
        input_idx += 1
    else:
        return True     


def max(input: list[int]) -> int:    
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    input_idx: int = 0
    largest: int = input[0]
    while input_idx < len(input):
        if input[input_idx] > largest:
            largest: int = input[input_idx]
        input_idx += 1
    return largest     


def is_equal(list1: list[int], list2: list[int]) -> bool:
    input_idx: int = 0
    while len(list1) == len(list2) and input_idx < len(list1):
        if list1[input_idx] != list2[input_idx]:
            return False
        input_idx += 1
    else:
        return True