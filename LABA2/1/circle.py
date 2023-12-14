from shape import Shape, random_color
import turtle


# Define a Circle class that inherits from the Shape base class
class Circle(Shape):
    def __init__(self, x, y, radius):
        # Constructor to initialize the Circle object with position and radius
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y - self.radius)
        turtle.pendown()
        turtle.pencolor(random_color())
        turtle.circle(self.radius)
