from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

        self.speed("fastest")
        self.setpos(pos, 0)

    def move_up(self):
        y_pos = self.ycor()
        new_y = self.ycor() + 20
        if y_pos < 260:

            self.goto(self.xcor(), new_y)

    def move_down(self):

        y_pos = self.ycor()
        new_y = self.ycor() - 20
        if y_pos > -260:
            self.goto(self.xcor(), new_y)
