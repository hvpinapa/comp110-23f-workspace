"""EX03 - Wordle!"""
__author__ = "730403031"

# Color code of boxes / Declaring secret word
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_word: str = "codes"

# Declaring function that describes searching string for correct characters, reporting a bool
def contains_char(any_len: str, sng_char: str) -> bool:
    """Determines if single character is found at any index of string."""

    assert len(sng_char) == 1
    i: int = 0
    while i < len(any_len):
        if sng_char == any_len[i]:
            return True
        i += 1
    return False

# Declaring function that creates emoji boxes to identify the placement of guess relative to secret
def emojified(guess: str, secret: str) -> str:
    """Determines color code of emoji to the guess."""

    assert len(guess) == len(secret)
    box_check: str = ""
    idx: int = 0
    while idx < len(secret):
        tried_chr: bool = contains_char(secret, guess[idx])
        if guess[idx] == secret[idx]:
            box_check += GREEN_BOX
        elif tried_chr == True:
            box_check += YELLOW_BOX
        else:
            box_check += WHITE_BOX
        idx += 1
    return box_check

# Declaring a function that allows user to input a guess of correct char length
def input_guess(exp_len: int) -> str:
    """Determining whether guess is at the expected length."""
    exp_guess: str = input(f"Enter a {exp_len} character word: ")
    guess_len: int = len(exp_guess)
    while guess_len != exp_len:
        exp_guess = input(f"That wasn't {exp_len} chars! Try again: ")
        guess_len = len(exp_guess)
    return exp_guess

# Building the main game using previous functions
def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        real_guess: str = input_guess(len(secret_word))

        if real_guess == secret_word:
            print(emojified(real_guess, secret_word))
            print(f"You won in {turns}/6 turns!")
            return
        else:
           print(emojified(real_guess, secret_word))
           turns += 1
        if turns > 6:
            print("X/6 - Sorry, try again tomorrow!")
            return

# Defining game to run as a module
if __name__ == "__main__":
    main()
