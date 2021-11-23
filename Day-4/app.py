import random

# * Head or tail

# num = random.randint(0, 1)

# if num == 0:
#     print('Head')
# else:
#     print('Tail')


# * Who's gonna pay the bill

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# random_num = random.randint(0, len(names)-1)

# print(f'Today bill is gonna to be paid by {names[random_num]} 😁 ')


# * Treasure map

# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")

# position = input("Where do you want to put the treasure? ")

# column = int(position[0])
# row = int(position[1])

# map[row-1][column-1] = 'X'
# print(f"{row1}\n{row2}\n{row3}")


# * Rock Paper  Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


posiibilities = [rock, paper, scissors]

rand_num = random.randint(0, 2)

computer_choice = posiibilities[rand_num]

user_num = int(input(
    'What do you choose? Type 0 for Rock, Type 1 for Paper, Type 2 for scissors: '))

user_choice = posiibilities[user_num]

if user_choice == rock and computer_choice == scissors:
    print(user_choice, computer_choice, 'You win\n')

elif user_choice == scissors and computer_choice == rock:
    print(user_choice, computer_choice, 'You lose\n')

elif user_choice == rock and computer_choice == paper:
    print(user_choice, computer_choice, 'You lose\n')

elif user_choice == paper and computer_choice == rock:
    print(user_choice, computer_choice, 'You win\n')

elif user_choice == scissors and computer_choice == paper:
    print(user_choice, computer_choice, 'You win\n')

elif user_choice == paper and computer_choice == scissors:
    print(user_choice, computer_choice, 'You lose\n')
elif user_choice == computer_choice:
    print(user_choice, computer_choice, 'You\'re equal')
