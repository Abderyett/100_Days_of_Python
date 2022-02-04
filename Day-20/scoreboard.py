from turtle import Turtle
FONT = ("arial", 24, "normal")
ALIGNEMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):

        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.clear()
        self.write(f"Score : {self.score} ",
                   align=ALIGNEMENT, font=FONT)

        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score} ",
                   align=ALIGNEMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.",
                   align=ALIGNEMENT, font=FONT)
