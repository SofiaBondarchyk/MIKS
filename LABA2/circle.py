# circle.py
from shape import Shape, random_color
import turtle

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y - self.radius)
        turtle.pendown()
        turtle.pencolor(random_color())
        turtle.circle(self.radius)
