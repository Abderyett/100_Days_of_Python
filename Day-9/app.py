import os
# Dictionaries

programming_dictionaries = {
    "name": "hello",
    123: "one two three"

}

# * Retriving Data from dictionary

# print(programming_dictionaries["name"])


# * Adding Data to Dictionary
programming_dictionaries["loop"] = {
    "Is an action doing something over and over again"}

# * Create an empty dictionary

empty_dictionary = {}

# * Wipe an existing dictionary
# programming_dictionaries = {}

# print(programming_dictionaries)

# * Edit Dictionary
programming_dictionaries["name"] = "Jesse"

# * Loop in Dictionaries

# for key in programming_dictionaries:
# print(key)
# print(programming_dictionaries[key])


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62}
student_grades = {}

for key in student_scores:
    if student_scores[key] >= 91 and student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        student_grades[key] = "Exceeds expectation"
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"


# print(student_grades)

# *  Nesting
# travel_log = {

#     "Italy": ["Florence", "Rome", "Pise", "Milan"],
#     "Spain": {"visited_cities": ["Barcelona", "Madrid"]}
# }


# *  Nesting Dictionary List

# travel_log = [

#     {"country": "France", "visited_cities": [
#         "Paris", "Lille", "Dijon"], "num_visit":3},

#     {"country": "Italy", "visited_cities": [
#         "Florence", "Rome", "Pise", "Milan"], "num_visit":5},

#     {"country": "Spain", "visited_cities": [
#         "Barcelona", "Madrid"], "num_visit":4}


# ]

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country_name, num_visits, list_cities):
    travel_log.append(
        {"country": country_name, "visits": num_visits, "cities": list_cities})


# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


# Auction Programm

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


isBider = True

participants = []
single_participant = {}


def add_participant(participan_name, bid_amount):

    participants.append({"name": participan_name, "bid": bid_amount})


while isBider:

    name = input("What's your name? : ")
    bid = int(input("What's your bid? : $"))
    add_participant(participan_name=name, bid_amount=bid)

    response = input("Are there any other bidders? Type 'yes or 'no' ").lower()
    clearConsole()
    if response == "no":
        isBider = False


amounts_of_bids = []
big_bid = ''

for bider in participants:
    amounts_of_bids.append(bider["bid"])
    if len(amounts_of_bids) == len(participants):
        big_bid = max(amounts_of_bids)
    if bider['bid'] == big_bid:
        print(f"The winner is {bider['name']} with a bid of ${big_bid}")
