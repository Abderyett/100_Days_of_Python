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

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

column = int(position[0])
row = int(position[1])

map[row-1][column-1] = 'X'
print(f"{row1}\n{row2}\n{row3}")
