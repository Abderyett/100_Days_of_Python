import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S.States.GAME")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(725, 491)


turtle.shape(image)


data = pandas.read_csv("./50_states.csv")

is_state = True
count = 0

while is_state:
    answer_state = screen.textinput(
        title=f"State correct {count}/50", prompt="What's another state name ?").capitalize()
    found_state = data[data.state == answer_state]
    if found_state.empty:
        answer_state = screen.textinput(
            title=f"State correct {count}/50", prompt="What's another state name ?").capitalize()

    else:

        text = turtle.Turtle()
        text.ht()
        count += 1
        x_cord = found_state.x.to_list()
        y_cord = found_state.y.to_list()
        state_name = found_state.state.to_list()
        coordinates = x_cord+y_cord
        text.penup()
        text.goto(x_cord[0], y_cord[0])
        text.write(state_name[0])

# turtle.mainloop()
screen.exitonclick()
