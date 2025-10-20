"""
install all these libraries
----------------------------
pip3 or pin install pandas
pin install pyarrow

numpy
openpyxl
pandas
pyarrow
pyjanitor
ipykernel

Classes in Python are the foundation of object-oriented programming (OOP) — 
they let you group data (attributes) and behavior (methods) into a single, 
reusable blueprint for creating objects.

Concept	        Description	                                Example
-------         -----------                                 --------
Encapsulation	Bundle data + methods	                    Car class has attributes + methods
Reusability	    Create many instances	                    car1, car2 from Car
Inheritance	    Build on existing classes	                ElectricCar(Car)
Polymorphism	Same method name, different behavior	    Dog.speak() and Cat.speak()
Abstraction	    Hide internal details	                    display_info() method



References:
    https://www.youtube.com/watch?v=tmY6FEF8f1o (Keith Galli - OOP Video)
    https://github.com/KeithGalli/python-classes-tutorial
    https://github.com/KeithGalli/complete-pandas-tutorial/blob/master/tutorial.ipynb
    https://numpy.org/doc/stable/reference/routines.linalg.html
"""

# Import library

#Visual library of Python
import turtle

# =============================================================================================
#                              INTRODUCTION TO CLASSES
# =============================================================================================

class Polygon:
    def __init__(self, sides, name, size=200, color="green", line_thickness=3):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles = (self.sides-2)*180
        self.angle = self.interior_angles/self.sides

    #Class level methods
    def draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180-self.angle)
       
# Not the class method
def draw_function(sides, size, angle, line_thickness, color):
    turtle.color(color)
    turtle.pensize(line_thickness)
    for i in range(sides):
        turtle.forward(size)
        turtle.right(180-angle)
    turtle.done()        

square = Polygon(4,"Square")
pentagon = Polygon(5,"Pentagon")
octagon = Polygon(8,"Octagon", color="red")

#draw_function(6,20,108,4,"red")
#octagon.draw()

# =============================================================================================
#                              INHERITANCE AND SUBCLASSING
# =============================================================================================

class Square(Polygon):
	def __init__(self, size=100, color="black", line_thickness=3):
		super().__init__(4, "Square", size, color, line_thickness)

    #Ovoeride super class method
	def draw(self):
		turtle.begin_fill()
		super().draw()
		turtle.end_fill()    

square = Square(color="blue")
square.draw()
turtle.done()