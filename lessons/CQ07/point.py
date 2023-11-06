"""Creating and Comparing Similar Methods but with Mutations!"""
from __future__ import annotations
__author__ = "730403031"


class Point:
    """Point Class, which constructs an ordered pair."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Constructor of Point class."""
        self.x = x_init
        self.y = y_init

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