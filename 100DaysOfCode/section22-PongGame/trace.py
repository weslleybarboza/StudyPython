from turtle import Turtle

COLOR = "white"
POSITION_Y_START = -460
POSITION_X_START = 0
POSITION_VARIATION = 40
NUMBER_OF_TRACE = 23

class Trace():

    def __init__(self):
        self.list_square = []
        self.set_trace()

    def set_trace(self):
        for square in range(NUMBER_OF_TRACE + 1):
            position_y = POSITION_Y_START + (square * POSITION_VARIATION)
            trace = Turtle(shape="square")
            trace.speed(0)
            trace.penup()
            trace.color(COLOR)
            trace.turtlesize(stretch_wid=1.2, stretch_len=0.2)
            trace.setposition(POSITION_X_START, position_y)
