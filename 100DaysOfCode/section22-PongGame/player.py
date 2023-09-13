from turtle import Turtle

COLOR = "white"
POSITION_VARIATION = 40
POSITION_Y_START = 0

class Player(Turtle):
    def __init__(self, position_x):
        super().__init__()

        self.trace = Turtle(shape="square")
        self.trace.speed(9)
        self.trace.penup()
        self.trace.color(COLOR)
        self.position_y = POSITION_Y_START
        self.position_x = position_x
        self.set_player()
        

    def set_player(self):
        position_y = self.position_y
        self.trace.turtlesize(stretch_wid=4, stretch_len=0.6)
        self.trace.setposition(self.position_x , position_y)
        print(f"SET PLAYER POSITION: {self.trace.pos()}")

    def move_up(self):
        position_y = self.trace.position()[1]
        new_position_y = position_y + POSITION_VARIATION
        self.trace.setposition(self.position_x , new_position_y)

    def move_down(self):
        position_y = self.trace.position()[1]
        new_position_y = position_y - POSITION_VARIATION
        self.trace.setposition(self.position_x , new_position_y)
        