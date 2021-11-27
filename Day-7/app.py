import random

# * Hangman Game

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
display = []

for word in chosen_word:
    display += '_'

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Please guess a letter : ").lower()
for i in range(0, len(display)-1):
    if chosen_word[i] == guess:
        display[i] = guess


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


for i in range(0, len(chosen_word)-1):
    if chosen_word[i] == guess:
        print("Your Guess is right.")
    else:
        print("Your Guess is wrong")
print(chosen_word)
print(display)
