from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.fd(10)


screen.onkey(key="space", fun=forward)

screen.listen()
screen.exitonclick()
