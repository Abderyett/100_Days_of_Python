# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("chartreuse4")
# timmy.forward(100)
# my_screen = Screen()
# my_screen.exitonclick()

# from prettytable import PrettyTable

# table = PrettyTable()

# table.field_names = ["Name", "Age", "Gender"]
# table.add_row(["Jesse", 32, "Male"])
# table.add_row(["Bisouma", 31, "Female"])
# table.add_row(["Caroline", 2, "Female"])
# table.add_column("rank", [15, 12, 4])
# table.align = "l"

# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


order = CoffeeMaker()
money = MoneyMachine()
menu = Menu()


is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to drink ({options}) : ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        order.report()
        money.report()
    else:
        drink = menu.find_drink(choice)

        is_resource_sufficient = order.is_resource_sufficient(drink)
        is_payment_success = money.make_payment(drink.cost)
        if is_resource_sufficient and is_payment_success:
            order.make_coffee(drink)
