from art import logo


def fromat_name(f_name, l_name):
    full_name = f"{f_name} {l_name}"
    return full_name.title()


# print(fromat_name("jesse", "james"))


# Days In Month


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        if month == 2:
            return 29
    else:
        month -= 1
        return month_days[month]


# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# Docstrings a way to write about the functionality of function


def fromat_name(f_name, l_name):
    """Take afirst name and last name and return title version fo name"""
    full_name = f"{f_name} {l_name}"
    return full_name.title()


# print(fromat_name("jesse", "james"))


# * Calculator


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def devide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": devide,
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number ? :"))

    for operation in operations:
        print(operation)

    is_continue = True

    while is_continue:
        operation_symbol = input("Pick operation :")
        function = operations[operation_symbol]

        num2 = float(input("What's the next number ? :"))
        answer = function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_answer = input(
            f"Type 'y' to continue calculating with {answer}, or Type 'n' to exit. :  "
        ).lower()

        if continue_answer == "y":
            num1 = answer

        else:
            is_continue = False
            calculator()


calculator()
