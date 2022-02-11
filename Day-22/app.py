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
        ball.bounce_y()
    # Detect Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    # Detect if right paddle miss the ball
    if ball.xcor() > 380:
        ball.reset_position()
    # Detect if left paddle miss the ball
    if ball.xcor() < - 380:
        ball.goto(0, 0)
        ball.reset_position()


screen.exitonclick()
