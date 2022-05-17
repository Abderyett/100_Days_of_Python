# * 1- FileNotFound
# try:
#     file = open("Data.txt", "r")
#     a_dictionary = {"key": "value"}
#     value = a_dictionary["adfjkan"]

# except FileNotFoundError:
#     file = open("Data.txt", "w")
#     file.write("First writing on file")
# except KeyError as error_message:
#     print(f"That Key {error_message} doesn't exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.colse()
#     print("File closed")

# * 2-  IndexError

# fruits = ["banana", "orange", "apple"]
# fruit = fruits[3]

# 3- KeyError

# a_dictionary = {"key": "value"}
# value = a_dictionary["non_exist"]

# * 4- TypeError

# a = "abs"
# print(a+5)


# * Raise our own Error

# height = float(input("Height :"))
# weight = int(input("Weight :"))
# if height > 3:
#     raise ValueError(f"Human height should not be over {height} 🤨")

# bmi = weight/height**2
# print(bmi)


# * Exercise IndexError Handling

fruits = ["Apple", "Pear", "Orange"]

# TODO: Catch the exception and make sure the code runs without crashing.


# def make_pie(index):

#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except IndexError:
#         print("fruit pie")


# make_pie(4)


# * Exercise KeyError Handling

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        pass


print(total_likes)
