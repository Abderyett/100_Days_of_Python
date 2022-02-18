
# * Read file
# with open("my_file.txt") as file:

#     contents = file.read()

#     print(contents)


# * Write File
# a stand for append
with open("my_file.txt", mode="a") as file:

    contents = file.write("\nHello there")


# if the file doesn't exist and mode= w then it will be created
with open("my_file_2.txt", mode="w") as file:

    contents = file.write("\nA New file been created")
