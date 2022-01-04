MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }

while True:
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    if drink == "report":
        print(
            f"Water {resources['water']}ml\nMilk {resources['milk']}ml\nCoffee {resources['coffee']}g"
        )
    elif drink == "espresso" or drink == "latte" or drink == "cappuccino":
        print("Please insert coins.")

        quarter = int(input("how many quarters? : "))
        dimes = int(input("how many dimes? : "))
        nickles = int(input("how many nickles? : "))
        pennies = int(input("how many pennies? : "))
        total = 0.25 * quarter + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
        change = total - MENU[drink]["cost"]
        if total > MENU[drink]["cost"]:
            if drink == "espresso":
                print(MENU[drink]["ingredients"]["water"], "WATER")
                MENU[drink]["ingredients"]["water"] = (
                    resources["water"] - MENU[drink]["ingredients"]["water"]
                )
                MENU[drink]["ingredients"]["coffee"] = (
                    resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
                )

            elif drink == "latte" or drink == "cappuccino":
                MENU[drink]["ingredients"]["water"] = (
                    resources["water"] - MENU[drink]["ingredients"]["water"]
                )
                MENU[drink]["ingredients"]["coffee"] = (
                    resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
                )
                MENU[drink]["ingredients"]["milk"] = (
                    resources["milk"] - MENU[drink]["ingredients"]["milk"]
                )

            # print(f"Here is {change}$ in change")
            # print(f"Here is your {drink} ☕️, Enjoy! ")
        else:
            print("Sorry that's not enough money. Money refunded.")
