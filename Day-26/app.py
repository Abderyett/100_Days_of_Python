import random
import pandas as pd
numbers = [1, 2, 3, 4, 5]

new_list = [n*2 for n in numbers]

# print(new_list)

name = "Abderaouf"
words = [letter for letter in name]

# print(words)


numbers_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n*n for n in numbers_list]

# print(squared_numbers)

# * Return Even Number
results = [n for n in numbers_list if n % 2 == 0]

# print(results)


def list(extention):
    with open(extention, mode="r") as file:
        lines = file.read()
        list_of_lists = lines.splitlines()
        new_list = [int(n) for n in list_of_lists]
    return new_list


list_1 = list('./file1.txt')
list_2 = list('./file2.txt')

common_num = [l1 for l1 in list_1 if l1 in list_2]
# print(common_num)


# Dictionary comprehension

names = ["Alex", "Jesse", "Bob", "Eleonor", "Monica", "Michele"]

students_score = {student: random.randint(0, 100) for student in names}

# {new_key:new_value for (key, value) in dictionary.items()}
students_passed = {
    student: score for (student, score) in students_score.items() if score > 60}


# print(students_passed)

# Excercise Dictionary comprehension

sentences = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence_list = sentences.split()

dic_word_counter = {sentence: len(sentence)
                    for sentence in sentence_list}

# print(dic_word_counter)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: round(tem_c*9/5, 2)+32 for(day, tem_c) in weather_c.items()}

# print(weather_f)
df = pd.read_csv('./nato_phonetic_alphabet.csv')

# in order to display data like {"A":"Alpha","B":"Bravo",...}
phonetic_dic = {row.letter: row.code for(index, row) in df.iterrows()}


word = input("Please enter Word : ").upper()

splited__word = [phonetic_dic[letter] for letter in word]
print(splited__word)
