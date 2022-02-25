from turtle import Turtle
FONT = ("arial", 24, "normal")
ALIGNEMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):

        super().__init__()
        self.score = 0
        with open("my_file.txt") as data:
            self.hight_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.clear()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()

        self.write(f"Score: {self.score} High Score: {self.hight_score}",
                   align=ALIGNEMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.hight_score:
            self.hight_score = self.score
            with open("my_file.txt", mode="w") as file:
                file.write(f"{self.hight_score}")

        self.score = 0
        self.update_scoreboard()
