"""Creating and Comparing Similar Methods but with Mutations!"""
from __future__ import annotations
__author__ = "730403031"


class Point:
    """Point Class, which constructs an ordered pair."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Constructor of Point class."""
        self.x = x_init
        self.y = y_init

    def __str__(self) -> str:
        """Magic method to make output a string."""
        my_point: str = f"x: {self.x}; y: {self.y}"
        return my_point
    
    def __mul__(self, factor: int | float) -> Point:
        """Magic method to multiply the points by a factor."""
        new_x = self.x * factor
        new_y = self.y * factor
        new_point: Point = Point(new_x, new_y)
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Magic method to add to the points."""
        new_x = self.x + factor
        new_y = self.y + factor
        new_point: Point = Point(new_x, new_y)
        return new_point
    
    def scale_by(self, factor: int) -> None:
        """Method that mutates Point class."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Method that belongs to Point class, but creates new Point."""
        new_x = self.x * factor
        new_y = self.y * factor
        new_point: Point = Point(new_x, new_y)
        return new_point