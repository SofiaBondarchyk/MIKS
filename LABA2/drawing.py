# drawing/drawing.py
import random
import turtle
import colorsys

def random_color():
    r, g, b = [int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1)]
    return "#{:02X}{:02X}{:02X}".format(r, g, b)

def create_random_shape():
    # Ваша реалізація тут
    pass
