import random
from turtle import Turtle, Screen
import random

pen = Turtle()

colors = ['#CCCCFF', '#DFFF00', '#FFBF00', '#FF7F50', '#DE3163', '#9FE2BF', '#40E0D0', '#6495ED']

def draw_shape(num_side):
    angle = 360/num_side
    pen.color(random.choice(colors))
    for _ in range(num_side):
        pen.forward(200)
        pen.right(angle)

for side in range(3, 11):
    draw_shape(side)