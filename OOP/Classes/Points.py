"""
OOP Shapes Example using the Turtle and Matplotlib Libraries
============================================================

This script demonstrates core Object-Oriented Programming (OOP) concepts in Python:
Encapsulation, Inheritance, Polymorphism, Reusability, and Abstraction — illustrated
through geometric objects (`Point`, `Polygon`, and `Square`) using both `turtle` and
`matplotlib`.

In this version, operator overloading is demonstrated in the `Point` class by redefining
the `+` operator, allowing two points to be added or a point to be shifted by a constant.

Libraries to Install:
---------------------
Use pip to install the required libraries:
    pip install numpy openpyxl pandas pyarrow pyjanitor ipykernel matplotlib

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
    - https://www.geeksforgeeks.org/python/operator-overloading-in-python/ (# Operator overloading cheatsheet)
"""

import turtle
import matplotlib.pyplot as plt


# =============================================================================================
#                               CLASS DEFINITIONS
# =============================================================================================


class Point:
    """
    Represents a 2D point that can be plotted and supports operator overloading.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
        color (str): The color used when plotting the point. Defaults to 'red'.
        size (int): The marker size for the point in the plot. Defaults to 10.
    """

    def __init__(self, x: float, y: float, color: str = "red", size: int = 10):
        """
        Initialize a new Point instance.

        Args:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
            color (str, optional): Color of the point marker. Defaults to 'red'.
            size (int, optional): Size of the point marker. Defaults to 10.
        """
        self.x = x
        self.y = y
        self.color = color
        self.size = size

    def __add__(self, other):
        """
        Overload the '+' operator to add two points or shift a point by a scalar.

        If another Point is provided, adds their x and y coordinates.
        If a scalar (int or float) is provided, adds it to both coordinates.

        Args:
            other (Point or float): Another point or a scalar value.

        Returns:
            Point: A new Point instance representing the sum.
        """
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y
            return Point(x, y, color=self.color, size=self.size)
        elif isinstance(other, (int, float)):
            x = self.x + other
            y = self.y + other
            return Point(x, y, color=self.color, size=self.size)
        else:
            raise TypeError("Operand must be of type Point, int, or float")

    def plot(self):
        """
        Plot the point using matplotlib.

        This method uses a scatter plot to visualize the point in 2D space.
        """
        plt.scatter(self.x, self.y, c=self.color, s=self.size)
        plt.text(
            self.x + 0.05,
            self.y + 0.05,
            f"({self.x}, {self.y})",
            fontsize=9,
            color=self.color,
        )


# =============================================================================================
#                               INHERITANCE AND SUBCLASSING
# =============================================================================================

# (You can add subclasses here in future versions, e.g., 3DPoint or ColoredPoint.)


# =============================================================================================
#                               MAIN EXECUTION
# =============================================================================================

if __name__ == "__main__":
    # Create two Point instances
    a = Point(1, 3, color="blue")
    b = Point(2, 4, color="green")

    # Demonstrate operator overloading: Add two points
    c = a + b

    # Demonstrate scalar addition: Shift point 'a' by +2
    d = a + 2

    # Plot all points
    a.plot()
    b.plot()
    c.plot()
    d.plot()

    # Configure plot appearance
    plt.title("Point Class Demonstration with Operator Overloading")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.axis("equal")

    # Display the plot
    plt.show()
