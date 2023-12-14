import turtle
import random
from line import Line
from rectangle import Rectangle
from circle import Circle

# Function to create a random shape (Line, Rectangle, or Circle)
def create_random_shape():
    shape_types = [Line, Rectangle, Circle]
    random_shape_type = random.choice(shape_types)
    if random_shape_type == Line:
        # Generate random coordinates for Line
        x1, y1, x2, y2 = random.randint(-200, 200), random.randint(-200, 200), random.randint(-200, 200), random.randint(-200, 200)
        return Line(x1, y1, x2, y2)
    elif random_shape_type == Rectangle:
        # Generate random parameters for Rectangle
        x, y, width, height = random.randint(-200, 200), random.randint(-200, 200), random.randint(10, 100), random.randint(10, 100)
        return Rectangle(x, y, width, height)
    else:
        # Generate random parameters for Circle
        x, y, radius = random.randint(-200, 200), random.randint(-200, 200), random.randint(10, 100)
        return Circle(x, y, radius)

# Set turtle speed
turtle.speed(1)

# Create and draw a random number of shapes
for _ in range(random.randint(1, 10)):
    shape = create_random_shape()
    shape.draw()

# Exit on click
turtle.exitonclick()
