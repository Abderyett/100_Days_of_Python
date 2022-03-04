
# * Read file
with open("../../Desktop/my_file_2.txt") as file:

    contents = file.read()

    print(contents)


# * Write File
# a stand for append
# with open("my_file.txt", mode="a") as file:

#     contents = file.write("\nHello there")


# if the file doesn't exist and mode= w then it will be created
# with open("my_file_2.txt", mode="w") as file:

#     contents = file.write("\nA New file been created")


# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
    # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


f = open("Day-24/Input/Names/invited_names.txt", "r")
lines = f.readlines()

for i in range(0, len(lines)):
    with open("Day-24/Input/Letters/starting_letter.txt", mode="r") as letter:
        letter_data = letter.read()
        stripped_name = lines[i].strip()

    letter_data = letter_data.replace("[name]", stripped_name)
    with open(f"Day-24/Output/ReadyToSend/letter_for_{lines[i]}.txt", mode="w") as file:
        file.write(letter_data)
        print(letter_data)
