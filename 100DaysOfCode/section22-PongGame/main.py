from turtle import Screen
from trace import Trace
from player import Player

SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1500
SCREEN_COLOR = "black"
SCREEN_TITLE = "Welcome to Pong Game"


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title(SCREEN_TITLE)
screen.bgcolor(SCREEN_COLOR)


# TODO: create the screen with vertical line
# trace = Trace()
# TODO: create the player1 object - Player. Allow to control

player = Player()

screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.listen()

# TODO: CREATE THE player2 object - PC

computer = Player()

# TODO: create the boll
# TODO: detect the collision with wall and bounce
# TODO: detect the collision with paddle
# TODO: detect when paddle misses
# TODO: keep scoreboard

screen.exitonclick()
