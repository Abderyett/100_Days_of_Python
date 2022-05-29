##################### Extra Hard Starting Project ######################
import random
import datetime as dt
import pandas as pd
import smtplib as smtplib
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

my_email = 'abderyetttesting@hotmail.com'
password = '123456789@()'

today = dt.date.today()
day = today.day
month = today.month
today_tuple = (month, day)

# Read birthdays.csv with pandas
data = pd.read_csv('./birthdays.csv')

birthdday_dic = {(data_row['month'], data_row['day'])
                  : data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdday_dic:
    birthday_person = birthdday_dic[today_tuple]

    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter:
        contents = letter.read()
        contents.replace('[NAME]', birthday_person["name"])
        print(contents)
    with smtplib.SMTP('smtp-mail.outlook.com') as connection:
        connection.starttls()

        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person['email'], msg=f"Subject: Happy birthday!\n\n{contents}")

# with open(f'./letter_templates/letter_{rand_num}.txt', 'w') as letter:
#     letter.write(text)
#     print(text)

# 4. Send the letter generated in step 3 to that person's email address.
