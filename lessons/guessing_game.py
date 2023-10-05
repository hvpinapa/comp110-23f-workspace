"""Program that loops until you guess the right number"""

from random import randint

secret: int = randint(1,10)
num_of_tries: int = 0
max_tries: int = int(input("How many tries would you like? "))
guess: int = int(input("Guess a number between 1 and 10: "))
tries_left = max_tries

while guess != secret and (num_of_tries < max_tries - 1):
    print("Wrong!")
    tries_left -= 1
    # If guess is out of bounds, let them know
    if (guess< 1) or (guess > 10):
        print("That's not between 1 and 10!")
    # If guess is too low, tell them
    if guess < secret:
        print("Too low!")
    # If guess is too high, tell them
    else:
        print("Too high!")
# Counting number of tries left
    if tries_left > 1:
        print(f"~~~ You have {tries_left} tries left! ~~~")
    elif tries_left == 1:
        print(f"~~~ You have {tries_left} try left ~~~")
 # Ask for different guess       
    guess = int(input("Guess again: "))
    num_of_tries += 1
  
    
# If I've reached this point, guess == secret
if guess == secret:
    print("You guessed correctly!")
else:
    print("_________________________________")
    print("That was incorrect! You Lose! :(")
