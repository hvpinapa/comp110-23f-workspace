"""EX02 - One-Shot Wordle."""
__author__ = "730403031"

# Establishing Secret & Prompting a Guess
secret_word: str = "python"
i: int = len(secret_word)
guess: str = input(f"What is your {i} letter guess? ")

while len(guess) != i:
    guess: str = input(f"That was not {i} letters! Try again: ")

#Initializing Color Boxes
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

#Establishing variables for index check
idx: int = 0
box_check: str = ""

#Logic Behind Index Check for Positions in Secret Word
while idx < i:
    #Check if index is the same -- green box
    if guess[idx] == secret_word[idx]:
        box_check += GREEN_BOX

    #Check if index is in string but diff position -- yellow box
    else:
        alt_idx: int = 0
        guess_chr: bool = False
        while not guess_chr and (alt_idx < i):
            if guess[idx] == secret_word[alt_idx]:
                guess_chr = True
                box_check += YELLOW_BOX
            alt_idx += 1

    #Check if index is not in the string -- white box
        if not guess_chr:
            box_check += WHITE_BOX

    idx += 1     
print (box_check) 

#Output Logic Behind Guess
if guess == secret_word:
    print("Woo! You got it!")        
else:
    print ("Not quite. Play again soon!")
