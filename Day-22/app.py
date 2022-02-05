from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
paddle = Paddle(350)
paddle2 = Paddle(-350)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()


screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")


screen.exitonclick()
