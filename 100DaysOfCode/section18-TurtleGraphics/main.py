from turtle import Turtle, Screen

turtle = Turtle()

turtle.shape("turtle")
turtle.color("green")
turtle.resizemode("auto")

pendown = True
for _ in range(50):
    turtle.forward(10)
    if pendown:
        turtle.penup()
        pendown = False
    else:
        turtle.pendown()
        pendown = True


screen = Screen()
screen.exitonclick()
