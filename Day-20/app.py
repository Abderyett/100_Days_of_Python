import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

screen.title("Snake Game")

snake = Snake()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_continnue_moving = True
while is_continnue_moving:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # to imitate real snake move and be able to turn the head of snake and followed by body


screen.exitonclick()
