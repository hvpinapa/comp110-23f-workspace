"""Practicing writing a function"""

def mimic(my_words: str) -> str:
    """Given the string my_word, outputs same string"""
    return my_words

# Calling mimic function
mimic("Help!")

print(mimic("Help!"))

my_words: str = "Help!"
response: str = mimic(my_words)
print(response)