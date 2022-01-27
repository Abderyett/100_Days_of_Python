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
    time.sleep(1)
    # to imitate real snake move and be able to turn the head of snake and followed by body
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].fd(20)

screen.exitonclick()
