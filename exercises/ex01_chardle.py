"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730403031"

# Prompting for Inputs / Exiting Early for Invalid Inputs
count_char: int = 0

word_input: str = input("Enter a 5-character word: ")
if len(word_input) != 5:
    print("Error: Word must contain 5 characters")
    exit()

char_input: str = input("Enter a single charcter: ")
if len(char_input) != 1:
    print("Error: Character must be a single charcter")
    exit()

print("Searching for " + char_input + " in " + word_input)

# Checking Indices for Matches
if char_input == word_input[0]:
    print(char_input + " found at index 0")
    count_char = count_char + 1

if char_input == word_input[1]:
    print(char_input + " found at index 1")
    count_char = count_char + 1

if char_input == word_input[2]:
    print(char_input + " found at index 2")
    count_char = count_char + 1

if char_input == word_input[3]:
    print(char_input + " found at index 3")
    count_char = count_char + 1

if char_input == word_input[4]:
    print(char_input + " found at index 4")
    count_char = count_char + 1

# Counting Matching Indices
if int(count_char) == 1:
    print(str(count_char) + " instance of " + char_input + " found in " + word_input)

if int(count_char) > 1:
    print(str(count_char) + " instances of " + char_input + " found in " + word_input)

if int(count_char) == 0:
    print("No instances of " + char_input + " found in " + word_input)
