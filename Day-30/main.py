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

height = float(input("Height :"))
weight = int(input("Weight :"))
if height > 3:
    raise ValueError(f"Human height should not be over {height} 🤨")

bmi = weight/height**2
print(bmi)
