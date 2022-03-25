import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S.States.GAME")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(
    title="Guess the state", prompt="What's another state name ?").capitalize()

data = pandas.read_csv("./50_states.csv")
found_state = data[data.state == answer_state]
print(found_state)


screen.exitonclick()
