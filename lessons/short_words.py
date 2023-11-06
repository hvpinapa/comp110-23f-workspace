"""Quiz 2 Practice Program ~ Short words."""
__author__ = "730403031"


def short_words(list1: list[str]) -> list[str]:
    """Returns a list of words shorter than 5 characters, and prints words that are 5 characters or longer."""
    final_list: list[str] = []
    i: int = 0
    while i < (len(list1)):
        if len(list1[i]) < 5:
            final_list.append(list1[i])
        else:
            print(f"{list1[i]} is too long!")
        i += 1
    return final_list