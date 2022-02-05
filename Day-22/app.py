from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
paddle = Paddle(370)
paddle2 = Paddle(-370)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)


screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")


is_game_on = True
while is_game_on:
    screen.update()


screen.exitonclick()
