from shape import Shape, random_color
import turtle


class Line(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        turtle.penup()
        turtle.goto(self.x1, self.y1)
        turtle.pendown()
        turtle.pencolor(random_color())
        turtle.goto(self.x2, self.y2)
