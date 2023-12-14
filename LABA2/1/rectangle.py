from shape import Shape, random_color
import turtle


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
         # Constructor for Rectangle class.
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.pencolor(random_color())
        for _ in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)
