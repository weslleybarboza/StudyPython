from turtle import Screen
from player import Player
from ball import Ball
from time import sleep

SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1500
SCREEN_COLOR = "black"
SCREEN_TITLE = "Welcome to Pong Game"
POSITION_X_START_LEFT = -720
POSITION_X_START_RIGHT= 720

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title(SCREEN_TITLE)
screen.bgcolor(SCREEN_COLOR)
screen.listen()

l_paddle = Player(position_x=POSITION_X_START_LEFT)
r_paddle = Player(position_x=POSITION_X_START_RIGHT)
ball = Ball()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

# TODO: detect when paddle misses
# TODO: keep scoreboard


game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()
    ball.move()

    print(f"L POSICAO: {l_paddle.pos()}")
    print(f"R POSICAO: {r_paddle.pos()}")

    # detect the collision with wall and bounce
    y_limit_max = (SCREEN_HEIGHT * 0.95) / 2
    y_limit_min = y_limit_max * -1
    
    if ball.ycor() > y_limit_max or ball.ycor() < y_limit_min:
        ball.bounce()

# TODO: detect the collision with paddle

    print(r_paddle.pos())
    print(ball.position())
    print(f'colision - dist: {ball.distance(r_paddle)}')

    
    # if ball.distance(r_paddle) < 50:
    #     print(f'colision - dist: {ball.distance(r_paddle)}')
    game_is_on = False

screen.exitonclick()
