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

angle = [0, 90, 180, 270]

pen.speed(0)
pen.pensize(15)

def draw_shape(num_side):
    for _ in range(num_side):
        pen.color(random_color())
        pen.forward(50)
        pen.seth(random.choice(angle))

for side in range(3, 200):
    draw_shape(side)