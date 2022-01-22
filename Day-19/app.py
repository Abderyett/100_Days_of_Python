from turtle import Turtle, Screen
import random
# tim = Turtle()


# def forward():
#     tim.fd(10)


# screen.onkey(key="space", fun=forward)

# * ============================ Etch sketch app =============================
# tim.speed(6)


def forward():
    tim.fd(20)


def backward():
    tim.bk(20)


def counter_clockwise():

    new_heading = tim.heading()+10
    tim.setheading(new_heading)


def clockwise():

    new_heading = tim.heading()-10
    tim.setheading(new_heading)


def clear():

    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# screen.onkey(key="w", fun=forward)
# screen.onkey(key="s", fun=backward)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear)


# ? ========================== ** Turtle Race ** ================================================
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=500, height=400)

width = screen.screensize()[0]
height = screen.screensize()[1]


all_turtles = []
is_race_on = False

user_bet = screen.textinput(
    title="turtle race_name", prompt="Wich turtle will win the race, Choose color : ")
for clr in colors:
    height -= 100
    new_turtle = Turtle(shape="turtle")
    new_turtle.shapesize(2, 2)
    new_turtle.color(clr)
    new_turtle.penup()
    new_turtle.goto(-width+30, -height)
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        current_speed = random.randint(0, 10)
        turtle.fd(current_speed)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won, {winning_color} turtle is winnner !")
            else:
                print(f"You've loose, {winning_color} turtle is winnner !")


screen.listen()
screen.exitonclick()
