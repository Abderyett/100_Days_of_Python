import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

screen.title("Snake Game")


starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for pos in starting_position:

    new_segment = Turtle('square')
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(pos)

    segments.append(new_segment)


is_continnue_moving = True

while is_continnue_moving:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.fd(10)


screen.exitonclick()
