import random

import turtle as t

tim = t.Turtle()

t.colormode(255)
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


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# *  Challange 2
# tim.pensize(10)


def shapes_draw():
    for i in range(3, 11):
        chosed_color = random_color()
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
        chosed_color = random_color()
        tim.color(chosed_color)
        tim.forward(30)
        tim.setheading(angle)


# random_moves(50)

# *  Challange 4
tim.speed(0)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()
