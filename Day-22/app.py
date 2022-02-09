from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
ball = Ball()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)
r_paddle = Paddle(370)
l_paddle = Paddle(-370)

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    # Detect the colision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce()


screen.exitonclick()
