
# print('Welcome to rollercoaster')
# height = int(input('what is your height in cm ? :'))
# bill = 0

# if height > 120:
#     age = int(input('what is your age ? :'))
#     if age >= 18:
#         bill += 12
#         print('Your ticket will cost 12$')
#     elif age >= 12 and age < 18:
#         bill += 7
#         print('Your ticket will cost 7$')
#     else:
#         bill += 5
#         print('Your ticket will cost 5$')

#     want_photo = input('do you want to take photo Y or N ? :')
#     if want_photo == 'y':
#         bill += 3
#         print(f'You total bill is {bill}')
# else:
#     print('Sorry you can\'t ride')


# * Use modulo
# number = int(input('Wich number you want to check? :'))

# if number % 2 == 0:
#     print(f'Your number {number} is even')
# else:
#     print(f'Your number {number} is odd')


# * BMI Calculator 2.0

# height = float(input('enter you height in meters m :'))
# weight = float(input('Enter your weight in kg :'))

# bmi = int((weight) / (height**2))
# if bmi < 18.5:
#     print(f'your BMI is {bmi} and you are underweight')
# elif bmi >= 18.5 and bmi <= 25:
#     print(f'your BMI is {bmi} and you are normal weight')
# elif bmi >= 25 and bmi < 30:
#     print(f'your BMI is {bmi} and you are overweight')
# elif bmi >= 30 and bmi < 35:
#     print(f'your BMI is {bmi} and you are obese')
# else:
#     print(f'your BMI is {bmi} and you are cliniclly obese')


# * Leap Years

# year = int(input("Which year do you want to check? "))

# if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#     print('This Leap year')
# elif year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
#     print('This Leap year')
# else:
#     print('Not Leap year')


# * Pizza Order

# print('Welcome to Python Pizza Delivery Service')
# pizza_price = 0
# size = input('What size pizza do you want? S,M,L : ').upper()
# if size == 'S':
#     pizza_price += 15
# elif size == 'M':
#     pizza_price += 20
# elif size == 'L':
#     pizza_price += 25
# else:
#     print('Please enter the right size S or M or L : ')

# add_pepperoni = input('Do you want to add pepperoni? Y or N : ').upper()
# if add_pepperoni == 'Y':
#     if size == 'S':
#         pizza_price += 2
#     elif size == 'M' or size == 'L':
#         pizza_price += 3
# add_cheese = input('Do you want extra cheese? Y or N : ').upper()
# if add_cheese == 'Y':
#     pizza_price += 1
# print(f'Your total is {pizza_price}')


# * Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").upper()
name2 = input("What is their name? \n").upper()
count1 = 0
count2 = 0
count1 += name1.count('T')
count1 += name1.count('R')
count1 += name1.count('U')
count1 += name1.count('E')
count1 += name2.count('T')
count1 += name2.count('R')
count1 += name2.count('U')
count1 += name2.count('E')

count2 += name2.count('L')
count2 += name2.count('O')
count2 += name2.count('V')
count2 += name2.count('E')
count2 += name1.count('L')
count2 += name1.count('O')
count2 += name1.count('V')
count2 += name1.count('E')

total_count = int(f'{count1}{count2}')

if total_count < 10 or total_count > 90:
    print(
        f'Your score is {total_count}, you go together like coke and mentos.')

elif total_count >= 40 and total_count <= 50:
    print(f'Your score is {total_count}, you are alright together.')

else:
    print(f'Your score is {total_count}.')
