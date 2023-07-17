import random
from turtle import Turtle, Screen
import random

pen = Turtle()
pen.screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


pen.speed("fastest")
pen.pensize(1)

def draw_shape(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        pen.color(random_color())
        pen.circle(300)
        pen.setheading(pen.heading() + angle)


draw_shape(303)