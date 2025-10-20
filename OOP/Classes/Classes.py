"""
OOP Shapes Example using the Turtle Graphics Library
====================================================

This script demonstrates the core Object-Oriented Programming (OOP) concepts in Python:
Encapsulation, Inheritance, Polymorphism, Reusability, and Abstraction — illustrated
through a `Polygon` base class and a derived `Square` class that use the `turtle` module
to visualize geometric shapes.

Libraries to Install:
---------------------
Use pip to install the required libraries:
    pip install numpy openpyxl pandas pyarrow pyjanitor ipykernel

Concepts Overview:
------------------
Concept         Description                             Example
--------        ------------------------------           ------------------------------
Encapsulation   Bundle data and methods                  Car class with attributes + methods
Reusability     Create multiple instances                car1, car2 from Car
Inheritance     Extend existing classes                  ElectricCar(Car)
Polymorphism    Same method name, different behavior     Dog.speak() and Cat.speak()
Abstraction     Hide internal details                    display_info() method

References:
-----------
    - https://www.youtube.com/watch?v=tmY6FEF8f1o (Keith Galli - OOP Video)
    - https://github.com/KeithGalli/python-classes-tutorial
    - https://github.com/KeithGalli/complete-pandas-tutorial/blob/master/tutorial.ipynb
    - https://numpy.org/doc/stable/reference/routines.linalg.html
"""

import turtle

# =============================================================================================
#                               CLASS DEFINITIONS
# =============================================================================================


class Polygon:
    """
    Represents a polygon that can be drawn using Python's turtle graphics.

    Attributes:
        sides (int): Number of sides of the polygon.
        name (str): Name of the polygon (e.g., 'Square', 'Pentagon').
        size (int, optional): Length of each side. Defaults to 200.
        color (str, optional): Color of the polygon outline. Defaults to 'green'.
        line_thickness (int, optional): Thickness of the polygon edges. Defaults to 3.
        interior_angles (float): Total of all interior angles.
        angle (float): Exterior turning angle for turtle drawing.
    """

    def __init__(self, sides, name, size=200, color="green", line_thickness=3):
        """Initialize a polygon with sides, name, and visual properties."""
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles = (self.sides - 2) * 180
        self.angle = self.interior_angles / self.sides

    def draw(self):
        """Draw the polygon using turtle graphics."""
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for _ in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180 - self.angle)


def draw_function(sides, size, angle, line_thickness, color):
    """
    Draw a polygon without creating a class instance.

    Args:
        sides (int): Number of sides of the polygon.
        size (int): Length of each side.
        angle (float): Internal angle to turn at each vertex.
        line_thickness (int): Pen thickness.
        color (str): Outline color.
    """
    turtle.color(color)
    turtle.pensize(line_thickness)
    for _ in range(sides):
        turtle.forward(size)
        turtle.right(180 - angle)
    turtle.done()


# =============================================================================================
#                               INHERITANCE AND SUBCLASSING
# =============================================================================================


class Square(Polygon):
    """
    Represents a square shape derived from the Polygon base class.

    Inherits all attributes and methods from Polygon but overrides the `draw()` method
    to include fill functionality.
    """

    def __init__(self, size=100, color="black", line_thickness=3):
        """Initialize a square with custom size, color, and line thickness."""
        super().__init__(4, "Square", size, color, line_thickness)

    def draw(self):
        """Draw a filled square using turtle graphics."""
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()


# =============================================================================================
#                               MAIN EXECUTION
# =============================================================================================

if __name__ == "__main__":
    # Create instances of Polygon
    square = Polygon(4, "Square")
    pentagon = Polygon(5, "Pentagon")
    octagon = Polygon(8, "Octagon", color="red")

    # Example usage:
    # draw_function(6, 20, 108, 4, "red")
    # octagon.draw()

    # Create and draw a filled blue square using inheritance
    filled_square = Square(color="blue")
    filled_square.draw()
    turtle.done()
