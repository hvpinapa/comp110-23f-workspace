"""Testing our methods through calling Point!"""

from lessons.CQ07.point import Point

my_point: Point = Point(2.0, 3.0)

my_point.scale_by(2)
print(f"Mutated Point: ({my_point.x}, {my_point.y})")
my_new_point: Point = my_point.scale(3)
print(f"New Point: ({my_new_point.x}, {my_new_point.y}")

my_point: Point = Point()