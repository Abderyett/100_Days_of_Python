import time
from turtle import Screen
from snake import Snake
from food import Food

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

screen.title("Snake Game")

snake = Snake()
food = Food()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_continnue_moving = True
while is_continnue_moving:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # To detect th collision the food with snake head
    if snake.head.distance(food) < 15:
        food.refresh()


screen.exitonclick()
