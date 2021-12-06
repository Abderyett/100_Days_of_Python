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


print(student_grades)
