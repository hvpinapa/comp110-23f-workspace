"""EX06 ~ Dictionary Functions!"""
__author__ = "730403031"


# Creates an inverted dictionary; empty dictiionary initialized with {}
def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary that has the keys and values swapped at each index."""
    switch: dict[str, str] = {}
    for key in input_dict:
        value = input_dict[key]
        # Checking if value already associated with inverted dictionary, raises error for duplicates
        if value in switch:
            raise KeyError("Two of the same values in the dictionary!")
        # Inverting key and value and storing it
        switch[value] = key
    return switch


# Defines function to find the most popular color in a dictionary
def favorite_color(colors: dict[str, str]) -> str:
    """Returns a string of the most popular color amoung a dictionary of colors."""
    color_amt: dict[str, int] = {}
    max: int = 0
    pop_color: str = ''

    for name in colors:
        # Color associated with iterated name
        color_name = colors[name]
        # Checks if color already exists in dict, adds 1 if it does
        if color_name in color_amt:
            color_amt[color_name] += 1
        # Starting count for new color
        else:
            color_amt[color_name] = 1
        # Checking if current color occurs more than recent most popular color; updates popular color and max count
        if color_amt[color_name] > max or (color_amt[color_name] == max and color_name < pop_color):
            pop_color = color_name
            max = color_amt[color_name]
    return pop_color


# Define function to count the number of items in a given list
def count(keys: list[str]) -> dict[str, int]:
    """Returns the number of items in the dictionary."""
    library: dict[str, int] = {}
    for item in keys:
        # Check if item already exists; adds 1 if it does, otherwise initializes new item
        if item in library:
            library[item] += 1
        else:
            library[item] = 1
    return library


# Defines function that alphabetizes words in a list based on their first character
def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary of the alphabetization of words based off their first character."""
    sorted: dict[str, list[str]] = {}
    for word in words:
        initial_char = word[0].lower()
        # If the first character is already initialized in the dict, and appends word
        if initial_char in sorted:
            sorted[initial_char].append(word)
        # If the initial char is not in dict, creates a new key for it
        else:
            sorted[initial_char] = [word]
    return sorted


# Defines a function that updates the attendance dictionary to add students based on different days
def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Returns a mutated dictionary based on students that are present on different days."""
    # Checks if day is already initialized, appends student if True
    if day in attendance_log:
        attendance_log[day].append(student)
    # New day, as the key, initialized if not True, students can be added
    else:
        attendance_log[day] = [student]
    return attendance_log
