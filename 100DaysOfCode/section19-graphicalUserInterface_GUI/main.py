from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

turtle.speed(9)
screen.listen()


def move_forward():
    turtle.forward(10)


def counter_clockwise():
    turtle.left(10)


def clockwise():
    turtle.right(10)


def backwards():
    turtle.backward(10)


def reset():
    turtle.reset()


screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=counter_clockwise, key="a")
screen.onkeypress(fun=clockwise, key="d")
screen.onkeypress(fun=backwards, key="s")
screen.onkeypress(fun=reset, key="c")

screen.exitonclick()
