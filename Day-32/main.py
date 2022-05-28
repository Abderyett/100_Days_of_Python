##################### Extra Hard Starting Project ######################
import random
import datetime as dt
import pandas as pd
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
name = ''
rand_num = None
# Read birthdays.csv with pandas
data = pd.read_csv('./birthdays.csv')

dic = data.to_dict(orient="records")


today = dt.date.today()
day = today.day
month = today.month
rand_num = random.randint(1, 3)


for i in range(0, len(dic)):
    if dic[i]['day'] == day and dic[i]['month'] == month:
        name = dic[i]['name']


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
with open(f'./letter_templates/letter_{rand_num}.txt', 'r') as letter:
    text = letter.readlines()

    text = text[0].replace('[NAME]', name)
    print(text)

with open(f'./letter_templates/letter_{rand_num}.txt', 'a') as letter:
    letter.write(text)

# 4. Send the letter generated in step 3 to that person's email address.
