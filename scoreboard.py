from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.initialize()
        with open("data.txt", mode="r") as file:
            self.highscore = file.read()
        self.score = 0

    def initialize(self):
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def set_the_new_highscore(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
