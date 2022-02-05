from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()

        self.setpos(0, 0)

    def move(self):
        x_pos = self.xcor()+10
        y_pos = self.ycor()+10
        self.goto(x_pos, y_pos)
