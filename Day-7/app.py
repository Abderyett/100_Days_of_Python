import random
import hangman_art
import hangman_words

# * Hangman Game


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)
display = []

for word in chosen_word:
    display += '_'
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.


is_completed = False
lives = 6
print(hangman_art.logo)
while not is_completed:
    guess = input("Please guess a letter : ").lower()
    if guess in display:
        print(f'You\'re already guessed this letter "{guess}"')
    for i in range(0, len(display)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(f"{' '.join(display)}")

    if guess not in chosen_word and lives != 0:
        lives -= 1
        print(f'Oups wrong letter "{guess}" you loose a life 💀 ')

    elif lives == 0:
        print('Game Over 💥')
        lives = 0
        is_completed = True

    if lives <= 6:
        print(hangman_art.stages[lives])
        print(lives)
    if "_" not in display:
        is_completed = True
        print('You Win!! 🥳')


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


# for i in range(0, len(chosen_word)-1):
#     if chosen_word[i] == guess:
#         print("Your Guess is right.")
#     else:
#         print("Your Guess is wrong")
# print(chosen_word)
# print(display)
