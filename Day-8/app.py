import math
# def greet(name):
#     print(f'Hello {name}')
#     print('How do you do ? ')
#     print('isn\'t the weather nice today ?')


# greet('Angela')


def greet_with(name, location):
    print(f'Hi {name}!')
    print(f'what is like in {location}')


# greet_with('Jesse', 'Missouri')

# * Key word Argument

# greet_with(location='Missouri', name='Jesse')


# * Paint area calculator

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5


# def paint_calc(height, width, cover):
#     num_of_cans = math.ceil((height * width)/cover)
#     print(f'You\'ll need {num_of_cans} cans of paint.')


# paint_calc(height=test_h, width=test_w, cover=coverage)

# * Prime number

n = int(input("Check this number: "))


def prime_checker(number):
    list = []
    if n > 1:
        for i in range(2, n):
            if(n % i == 0):
                list.append(n)
    else:

        print(n, "is a prime number")

    if len(list) > 1:
        print('is not prime number')
    else:
        print("is a prime number")


prime_checker(number=n)
