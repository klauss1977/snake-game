from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()

    def score(self, score):
        self.clear()
        self.write(f"Score: {score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

