################### Scope ####################

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope


def drink_potion():
    potion_strength = 2
    # print(potion_strength)


# drink_potion()
# print(potion_strength)

# Global Scope
player_health = 10


def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    # drink_potion()


# print(player_health)

# There is no Block Scope

game_level = 3


def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    # print(new_enemy)


# Modifying Global Scope

enemies = 1


def increase_enemies():
    # print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"


from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

numbers = []
for i in range(0, 101):
    numbers.append(i)

random_num = random.choice(numbers)
print(f"Pssst, the correct answer is {random_num}")
attempts = 0


is_continue = True

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


def set_difficulty():

    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def reduce_attempts():

    return attempts - 1


turns = set_difficulty()
while is_continue and turns > 0:

    guess = int(input("Make a guess: "))
    if turns == 0:
        is_continue = False
        print("You've run out of guesses, you lose.")
    elif guess > random_num:
        print("To hight.")
        print("Guess again.")

        turns -= 1
    elif random_num > guess:
        print("To Low")
        print("Guess again.")

        turns -= 1
    else:
        print(f"You got it! the answer was {random_num} ")
        is_continue = False
    print(f"You have {turns} attempts remaining to guess the number.")
