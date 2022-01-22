from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# def forward():
#     tim.fd(10)


# screen.onkey(key="space", fun=forward)

# * Etch sketch app
tim.speed(6)


def forward():
    tim.fd(20)


screen.onkey(key="w", fun=forward)


def backward():
    tim.bk(20)


screen.onkey(key="s", fun=backward)


def counter_clockwise():

    new_heading = tim.heading()+10
    tim.setheading(new_heading)


screen.onkey(key="a", fun=counter_clockwise)


def clockwise():

    new_heading = tim.heading()-10
    tim.setheading(new_heading)


screen.onkey(key="d", fun=clockwise)


def clear():

    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(key="c", fun=clear)

screen.listen()
screen.exitonclick()
