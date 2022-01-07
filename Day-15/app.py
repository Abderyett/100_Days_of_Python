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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

resources["money"] = 0.0


def check_suficiant_resources(ingredients, drink):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"There is not enough {item} to make {drink}")
            return False

    return True


while True:

    drink = input("What would you like? (espresso/latte/cappuccino): ")

    if drink == "report":
        print(
            f"Water {resources['water']}ml\nMilk {resources['milk']}ml\nCoffee {resources['coffee']}g\nMoney {resources['money']}$"
        )

    elif drink == "espresso" or drink == "latte" or drink == "cappuccino":
        if check_suficiant_resources(MENU[drink]["ingredients"], drink):
            print("Please insert coins.")

            quarter = int(input("how many quarters? : "))
            dimes = int(input("how many dimes? : "))
            nickles = int(input("how many nickles? : "))
            pennies = int(input("how many pennies? : "))
            total = 0.25 * quarter + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
            change = total - MENU[drink]["cost"]
            if total > MENU[drink]["cost"]:
                if drink == "espresso":
                    resources.update(
                        {
                            "water": resources["water"]
                            - MENU[drink]["ingredients"]["water"]
                        }
                    )
                    resources.update(
                        {
                            "coffee": resources["coffee"]
                            - MENU[drink]["ingredients"]["coffee"]
                        }
                    )
                    print(MENU[drink]["cost"])
                    resources.update(
                        {"money": resources["money"] + MENU[drink]["cost"]}
                    )

                elif drink == "latte" or drink == "cappuccino":

                    resources.update(
                        {
                            "water": resources["water"]
                            - MENU[drink]["ingredients"]["water"]
                        }
                    )
                    resources.update(
                        {
                            "coffee": resources["coffee"]
                            - MENU[drink]["ingredients"]["coffee"]
                        }
                    )
                    resources.update(
                        {"milk": resources["milk"] - MENU[drink]["ingredients"]["milk"]}
                    )
                    resources.update(
                        {"money": resources["money"] + MENU[drink]["cost"]}
                    )
                else:
                    print(f"Please select correct drink")

                print(f"Here is {round(change,2)}$ in change")
                print(f"Here is your {drink} ☕️, Enjoy! ")
            else:
                print("Sorry that's not enough money. Money refunded.")
