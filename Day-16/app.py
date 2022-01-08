# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("chartreuse4")
# timmy.forward(100)
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Name", "Age", "Gender"]
table.add_row(["Jesse", 32, "Male"])
table.add_row(["Bisouma", 31, "Female"])
table.add_row(["Caroline", 2, "Female"])
table.add_column("rank", [15, 12, 4])
table.align = "l"

print(table)
