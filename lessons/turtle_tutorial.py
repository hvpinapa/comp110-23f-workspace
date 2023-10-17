"""This is a Tutorial on the Turtle Project!"""
__author__: "730403031"

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.color("green", "black")
leo.speed(50)
leo.hideturtle()

leo.penup()
leo.goto(-180, 0)
leo.pendown()

leo.begin_fill()
i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()


bob: Turtle = Turtle()
side_len: int = 350

id: int = 0
while id < 1000:
    bob.forward(side_len)
    bob.left(121)
    id += 1
    side_len *= 0.97

done()