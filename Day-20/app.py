import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()
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
        snake.extend()
        scoreboard.increase_score()
    # Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        scoreboard.reset()

    # Detect Collision  with tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
