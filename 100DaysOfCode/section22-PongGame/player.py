from turtle import Turtle

COLOR = "white"
POSITION_Y_PLAYER_START = -450
POSITION_Y_PC_START = -450
POSITION_X_START = -720
POSITION_VARIATION = 40


class Player:
    def __init__(self):
        self.trace = Turtle(shape="square")
        self.trace.speed(9)
        self.trace.penup()
        self.trace.color(COLOR)
        self.set_player()

    def set_player(self):
        position_y = POSITION_Y_PLAYER_START
        self.trace.turtlesize(stretch_wid=4, stretch_len=0.6)
        self.trace.setposition(POSITION_X_START, position_y)

    def move_up(self):
        position_y = self.trace.position()[1]
        new_position_y = position_y + POSITION_VARIATION
        self.trace.setposition(POSITION_X_START, new_position_y)

    def move_down(self):
        position_y = self.trace.position()[1]
        new_position_y = position_y - POSITION_VARIATION
        self.trace.setposition(POSITION_X_START, new_position_y)
        