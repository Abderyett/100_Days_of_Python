from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color('DarkGreen')

timmy_the_turtle.forward(100)

for _ in range(3):
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(100)


screen = Screen()
screen.exitonclick()
