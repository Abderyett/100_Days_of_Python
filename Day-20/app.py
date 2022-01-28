import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

screen.title("Snake Game")

snake = Snake()

is_continnue_moving = True
while is_continnue_moving:
    screen.update()
    time.sleep(1)

    snake.move()
    # to imitate real snake move and be able to turn the head of snake and followed by body


screen.exitonclick()
