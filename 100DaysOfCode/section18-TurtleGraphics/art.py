import colorgram
from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()
path_img = 'img.png'

turtle.speed(9)
turtle.pensize(1)
turtle.penup()
turtle.hideturtle()
turtle.setx(-400)
turtle.sety(-300)
forward_size = 50
dots_amount = 20

def extract_color(path_img, qty):
    """
    Extract a list of colors RGB based in an image.
    Inform the number of colors desired.
    """
    list_of_colors = []
    colors = colorgram.extract(path_img, qty)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color_rgb = (r, g, b)
        list_of_colors.append(color_rgb)
    return list_of_colors

list_of_color = extract_color(path_img, 34)

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def draw_points(colors, foward_size, dots_amount):
    for _ in range(1, dots_amount):
        color = random.choice(colors)
        turtle.dot(20, rgb_to_hex(color[0],color[1],color[2]))
        turtle.fd(foward_size)
        turtle.dot(20, rgb_to_hex(color[0],color[1],color[2]))


for _ in range(1, dots_amount + 1):
    draw_points(list_of_color, forward_size, dots_amount)
    turtle.setx(-400)
    turtle.sety(turtle.position()[1] + forward_size)

screen.exitonclick()

