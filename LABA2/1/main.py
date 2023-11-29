import turtle
import random
from line import Line
from rectangle import Rectangle
from circle import Circle


def create_random_shape():
    shape_types = [Line, Rectangle, Circle]
    random_shape_type = random.choice(shape_types)
    if random_shape_type == Line:
        x1, y1, x2, y2 = random.randint(-200, 200), random.randint(-200, 200), random.randint(-200, 200), random.randint(-200, 200)
        return Line(x1, y1, x2, y2)
    elif random_shape_type == Rectangle:
        x, y, width, height = random.randint(-200, 200), random.randint(-200, 200), random.randint(10, 100), random.randint(10, 100)
        return Rectangle(x, y, width, height)
    else:
        x, y, radius = random.randint(-200, 200), random.randint(-200, 200), random.randint(10, 100)
        return Circle(x, y, radius)

turtle.speed(1)

for _ in range(random.randint(1, 10)):
    shape = create_random_shape()
    shape.draw()
    
turtle.exitonclick()

