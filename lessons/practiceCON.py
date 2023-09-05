"""Conditional Pracitce Problem"""
"""Write a program that prints "Right" if my_number is 10 and "Wrong" if my_number is not 10"""

my_number_string: str = input("Guess a number: ")
my_number: int = int(my_number_string)
number: int = 10

if my_number == number:
    print("Right!")
else:
    print("Wrong")
