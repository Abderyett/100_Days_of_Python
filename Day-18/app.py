import random
import imp
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color('DarkGreen')

# Draw Square

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


colors = ["blue", "DarkOrange", "green", "DeepSkyBlue",
          "gold1", "orchid", "turquoise1", "purple2"]

# *  Challange 2
tim.pensize(10)


def shapes_draw():
    for i in range(3, 11):
        chosed_color = random.choice(colors)
        tim.color(chosed_color)
        for _ in range(i):

            tim.forward(100)
            tim.right(360/i)


# shapes_draw()


# * Challange 3:
def random_moves(steps):

    angles = [0, 90, 180, 270]

    for _ in range(steps):

        angle = random.choice(angles)
        chosed_color = random.choice(colors)
        tim.color(chosed_color)
        tim.forward(30)
        tim.setheading(angle)


random_moves(50)

# def triangle():
#     for _ in range(3):
#         tim.forward(100)
#         tim.right(120)


# triangle()


# def square():
#     for _ in range(4):
#         tim.forward(100)
#         tim.right(90)


# square()


# def pentagon():

#     for _ in range(5):
#         tim.forward(100)
#         tim.right(72)


# pentagon()


# def hexagon():
#     for _ in range(6):
#         tim.forward(100)
#         tim.right(60)


# hexagon()


# def heptagon():
#     for _ in range(7):
#         tim.forward(100)
#         tim.right(360/7)


# heptagon()


# def optagon():
#     for _ in range(8):
#         tim.forward(100)
#         tim.right(360/8)


# optagon()


# def nonagon():
#     for _ in range(9):
#         tim.forward(100)
#         tim.right(360/9)


# nonagon()


# def decagon():
#     for _ in range(10):
#         tim.forward(100)
#         tim.right(360/10)


# decagon()


screen = Screen()
screen.exitonclick()
