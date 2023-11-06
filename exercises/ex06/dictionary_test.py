"""EX07 ~ Test Functions for our Dictionary!"""
__author__ = "730403031"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


# Testing the invert function (3 cases + key error)
def test_invert_use_case1() -> None:
    """Testing single input for key and value in dict."""
    input_dict = {'a': 'v'}
    assert invert(input_dict) == {'v': 'a'}


def test_invert_use_case2() -> None:
    """Testing multiple inputs for the keys and values in the dict."""
    input_dict = {'a': 'v', 'c': 't', 'b': 'g'}
    assert invert(input_dict) == {'v': 'a', 't': 'c', 'g': 'b'}


def test_invert_edge_case() -> None:
    """Testing an empty dict."""
    input_dict = {}
    assert invert(input_dict) == {}


def test_invert_key_error() -> None:
    """Tests the key error in invert."""
    with pytest.raises(KeyError):
        input_dict = {'a': 'y', 'b': 'z', 'c': 'y'}
        invert(input_dict)


# Testing the favorite_color function (3 cases)
def test_favorite_color_expected_use_case1() -> None:
    """Testing single inputs in dict."""
    colors = {'Ann': 'red'}
    assert favorite_color(colors) == 'red'


def test_favorite_color_expected_use_case2() -> None:
    """Testing multiple inputs in dict."""
    colors = {'Ann': 'red', 'Bob': 'green', 'Jeff': 'green', 'Hari': 'blue'}
    assert favorite_color(colors) == 'green'


def test_favorite_color_edge_case() -> None:
    """Testing an empty case."""
    colors = {}
    assert favorite_color(colors) == ''


# Testing the count function (3 cases)
def test_count_expected_use_case1() -> None:
    """Testing a single input in the list to be output in the dictionary."""
    keys = ['apple']
    assert count(keys) == {'apple': 1}


def test_count_expected_use_case2() -> None:
    """Testing multiple inputs in the list."""
    keys = ['apple', 'banana', 'orange', 'apple', 'orange']
    assert count(keys) == {'apple': 2, 'banana': 1, 'orange': 2}


def test_count_edge_case() -> None:
    """Testing an empyt list."""
    keys = []
    assert count(keys) == {}


# Testing the alphabetizer function (3 cases)
def test_alphabetizer_expected_use_case1() -> None:
    """Testing the alphabetizer using a single input for key and value."""
    words = ['apple']
    assert alphabetizer(words) == {'a': ['apple']}


def test_alphabetizer_expected_use_case2() -> None:
    """Testing multiple inputs for varying letters and words."""
    words = ['apple', 'banana', 'agent', 'peach', 'pineapple']
    assert alphabetizer(words) == {'a': ['apple', 'agent'], 'b': ['banana'], 'p': ['peach', 'pineapple']}


def test_alphabetizer_edge_case() -> None:
    """Testing an empty list."""
    words = []
    assert alphabetizer(words) == {}


# # Testing the update_attendance function (3 cases)
def test_update_attendance_expected_use_case1() -> None:
    """Testing a case where we append one student to a single day."""
    attendance_log = {'Monday': ['Hari', 'Kayla'], 'Tuesday': ['Dontai']}
    day = 'Tuesday'
    student = 'Alyssa'
    assert update_attendance(attendance_log, day, student) == {'Monday': ['Hari', 'Kayla'], 'Tuesday': ['Dontai', 'Alyssa']}


def test_update_attendance_expected_use_case2() -> None:
    """Testing a case where we append a new name to a new day."""
    attendance_log = {'Monday': ['Hari', 'Kayla'], 'Tuesday': ['Dontai']}
    day = 'Wednesday'
    student = 'Alyssa'
    assert update_attendance(attendance_log, day, student) == {'Monday': ['Hari', 'Kayla'], 'Tuesday': ['Dontai'], 'Wednesday': ['Alyssa']}


def test_update_attendance_edge_case() -> None:
    """Testing the result of an empty log and appending empty days and names."""
    attendance_log = {}
    day = ''
    student = ''
    assert update_attendance(attendance_log, day, student) == {'': ['']}
