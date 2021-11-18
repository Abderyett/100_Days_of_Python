
# print('Welcome to rollercoaster')
# height = int(input('what is your height in cm ? :'))


# if height > 120:
#     age = int(input('what is your age ? :'))
#     if age >= 18:
#         print('Your ticket will cost 12$')
#     elif age >= 12 and age < 18:
#         print('Your ticket will cost 7$')
#     else:
#         print('Your ticket will cost 5$')
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

year = int(input("Which year do you want to check? "))

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print('This Leap year')
elif year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
    print('This Leap year')
else:
    print('Not Leap year')
