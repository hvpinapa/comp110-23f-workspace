"""EX05 - Space ~ A look at Home."""

from turtle import Turtle, colormode, Screen, done
from random import randint

__author__ = "730403031"

art: Turtle = Turtle()
art.speed(0)
colormode(255)


def main() -> None:
    """The entry point of my scene."""  
    bckgrd = Screen()
    bckgrd.bgcolor("black")
    
    # Return address for stars
    star_num: int = 50
    star_size: int = 50
    stars(star_num, star_size)
    
    # Return address for moon
    moon_rad: float = 40.0
    moon(art, -275.5, 226.5, moon_rad)

    # Return address for Earth w/out continents
    width: int = 200
    blue_earth(art, -150.0, -50.0, width)

    # Return address for North America
    na_earth(art, 30.0, 150.0)

    # Return address for Antarctica
    artic(art, -20.0, -210.0)

    # Return address for other continents
    other_cont(art, 75.0, 100.0)
    done()
    bckgrd.exitonclick()


# Function that gives the basis to draw a star
def star_draw(art: Turtle, x: float, y: float, size: float) -> None:
    """Draws a star of a particular size given an x and y coordinate."""
    art.penup()
    art.goto(x, y)
    art.pendown()
    art.color(240, 230, 70)
    
    art.begin_fill()

    # Gives angle and side length of the star
    angle: int = 140
    side: float = size * 0.25
   
    i: int = 0
    while i < 5:
        art.forward(side)
        art.right(angle)
        i += 1
    art.end_fill()


# Function that produces selected number of stars with a random placement
def stars(star_num: int, size: int) -> None:
    """Places drawn stars at the location and size specified."""
    stock: int = 0
    while stock < star_num:
        x: float = randint(-300, 300)
        y: float = randint(-200, 300)
        star_draw(art, x, y, size)
        stock += 1


# Function that draws a Moon
def moon(art: Turtle, xp: float, yp: float, rad: float) -> None:
    """Draws moon given an x and y coordinate with a selected radius."""
    art.penup()
    art.goto(xp, yp)
    art.setposition(xp, yp)
    art.pendown()
    art.color("white")
    art.begin_fill()
    art.circle(rad)
    art.end_fill()


# Function that draws Earth without land
def blue_earth(art: Turtle, x: float, y: float, width: int) -> None:
    """Draws circle that represents the earth with just the blue hue."""
    art.penup()
    art.setposition(x, y)
    art.goto(x, y)
    
    art.pendown()
    art.color("blue")
    art.begin_fill()
    art.circle(width)
    art.end_fill()


# Function that draws North America on Earth
def na_earth(art: Turtle, x: float, y: float) -> None:
    """Draws shapes to represent the continents on earth."""
    art.penup()
    art.goto(x, y)
    art.setposition(x, y)
    art.pendown()
    art.color("green")
    art.begin_fill()

    art.right(20)
    art.forward(150)
    art.right(90)
    art.forward(80)
    art.right(25)
    art.forward(45)
    art.left(15)
    art.forward(25)
    art.right(90)
    art.forward(10)
    art.right(15)
    art.forward(100)
 
    art.end_fill()


# Function that draws semi-circle representing the artic
def artic(art: Turtle, x: float, y: float) -> None:
    """Draws a semi-circle that represents Antarctica."""
    art.penup()
    art.goto(x, y)
    art.setposition(x, y)
    art.setheading(270.0)
    art.pendown()
    art.color(234, 244, 245)
    art.begin_fill()
    
    art.circle(65, -180)
    art.end_fill()


# Function for Eastern continents
def other_cont(art: Turtle, x: float, y: float) -> None:
    """Draws a landscape representing other lands on the Earth."""
    art.penup()
    art.goto(x, y)
    art.setposition(x, y)
    art.setheading(0.0)
    art.pendown()
    art.color("green")
    art.begin_fill()

    art.right(0)
    art.forward(80)
    art.left(120)
    art.forward(40)
    art.right(90)
    art.forward(45)
    art.right(88)
    art.forward(100)
    art.right(45)
    art.forward(150)
    art.right(20)
    art.forward(40)
    art.right(90)
    art.forward(150)
    art.right(70)
    art.forward(130)

    art.end_fill()


if __name__ == "__main__":
    main()