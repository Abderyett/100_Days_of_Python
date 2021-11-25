# * Loop Average Height


# height = input(
#     'What are the height of the student that you wanna to calculate ? :').split()


# for i in range(0, len(height)):
#     height[i] = int(height[i])
# sum = 0
# for n in height:
#     sum = sum + n

# average = sum/len(height)
# rounded_avg = round(average)

# print(f'The average height is {rounded_avg}')


# * Loop Height Score

# score = input(
#     'Input list of students Score ? :').split()


# for i in range(0, len(score)):
#     score[i] = int(score[i])


# max = 0
# for i in range(0, len(score)):
#     if i+1 < len(score):
#         if score[i] > score[i+1] and score[i] > max:
#             max = score[i]
#         elif score[i] < score[i+1] and score[i+1] > max:
#             max = score[i+1]
#         elif score[i] == score[i+1] and score[i+1] == max:
#             max = score[i]
#     elif i+1 > len(score) or i+1 == len(score):
#         print(f'The max num in this list is {max}')


# * Adding Evens
# total = 0
# for i in range(2, 101, 2):
#     total = total+i

# print(total)
# * Fizz Buzz Game
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FIZZBUZZ')

#     elif i % 3 == 0:
#         print('Fizz')

#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# *  Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


random_number = random.choice(symbols)

password = []

for i in range(1, nr_letters+1):
    password += random.choice(letters)

for i in range(0, nr_symbols+1):
    password += random.choice(symbols)

for i in range(1, nr_numbers+1):
    password += random.choice(numbers)


new_List = password.copy()
random.shuffle(new_List)

new_password = ''.join(new_List)

print(new_password)
