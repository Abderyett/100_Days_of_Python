
numbers = [1, 2, 3, 4, 5]

new_list = [n*2 for n in numbers]

# print(new_list)

name = "Abderaouf"
words = [letter for letter in name]

# print(words)


numbers_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n*n for n in numbers_list]

# print(squared_numbers)

# * Return Even Number
results = [n for n in numbers_list if n % 2 == 0]

# print(results)


def list(extention):
    with open(extention, mode="r") as file:
        lines = file.read()
        list_of_lists = lines.splitlines()
        new_list = [int(n) for n in list_of_lists]
    return new_list


list_1 = list('./file1.txt')
list_2 = list('./file2.txt')

common_num = [l1 for l1 in list_1 if l1 in list_2]
print(common_num)
