
print('Welcome to the tip calculator.')

total = float(input('What was the bill total? $ '))

num_people = int(input('How many peoples to split the bill '))

tip = int(input('What\'s percentage tip would you like to give? 10,12 or 15? '))
amount_to_pay = round((total/num_people) * (1+(tip/100)), 2)
print(f'Each person should pay: $ {amount_to_pay}')


# ? BMI Calculator

# height = float(input('enter you height in meters m :'))
# weight = float(input('Enter your weight in kg :'))

# bmi = int((weight) / (height**2))
# print(bmi)


# ?  Years Left

age = int(input('What is you current age ? : '))

days_left = (90*365) - (age * 365)
weeks_left = (90*52) - (age * 52)
months_left = (90*12) - (age * 12)

print(
    f'You have {days_left} days, {weeks_left} weeks, and {months_left} months')
