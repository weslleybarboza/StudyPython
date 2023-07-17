from turtle import Turtle, Screen
import random as r

is_race_on = False
screen = Screen()
screen_width=500
screen_height=400
screen.setup(width=screen_width, height=screen_height)
user_bet = screen.textinput(title="Make your bet", prompt="Which/ turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "blue", "purple"]

all_turtle = []

for idx, color in enumerate(colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    position_y = -100 + (idx * 50)
    new_turtle.goto(x=-230, y=position_y)
    all_turtle.append(new_turtle)

print(all_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        forward_size = r.randint(0, 10)
        turtle.forward(forward_size)

screen.exitonclick()