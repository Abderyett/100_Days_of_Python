import random
from art import logo
from art import vs
from game_data import data
import os

print(logo)

random_num = random.randint(0, len(data) - 1)


def clear():
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)


def pick_num():

    random_num = random.randint(0, len(data) - 1)

    return random_num


is_continue = True
score = 0

while is_continue:
    first_pick = data[pick_num()]
    second_pick = data[pick_num()]

    A = first_pick["follower_count"]
    B = second_pick["follower_count"]
    right_answer = ""

    if A > B:
        right_answer = "A"
    else:
        right_answer = "B"
    print(
        f"Compare A: {first_pick['name']}, {first_pick['description']}, from {first_pick['country']}"
    )

    print(vs)

    print(
        f"Compare B: {second_pick['name']}, {second_pick['description']}, from {second_pick['country']}"
    )

    answer = input("Who has more followers? Type 'A' or 'B' : ").upper()

    if answer == right_answer:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        is_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
