from turtle import Turtle

POSITION_X = 0
POSITION_Y = 270
FONT_NAME = "Arial"
FONT_SIZE = 20
FONT_TYPE = "normal"
FONT_COLOR = "white"
FONT_ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(POSITION_X, POSITION_Y)
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color(FONT_COLOR)
        self.speed("fastest")
        self.print_scoreboard()

    def print_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=False, align=FONT_ALIGN, font=(FONT_NAME, FONT_SIZE, FONT_TYPE))

    def print_gameover(self):
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER!", move=False, align=FONT_ALIGN, font=(FONT_NAME, FONT_SIZE, FONT_TYPE))
    def increase_score(self):
        self.clear()
        self.score += 1
        self.print_scoreboard()
