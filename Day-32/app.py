import smtplib
import datetime as dt
import random

my_email = 'abderyetttesting@hotmail.com'
password = '123456789@()'
day_quote = ''


now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()


print(day_quote)
if day_of_week == now.weekday():
    with open("./quotes.txt") as file:
        filecontents = file.readlines()
        filecontents = [line.strip() for line in filecontents]
        day_quote = random.choice(filecontents)
    with smtplib.SMTP('smtp-mail.outlook.com') as connection:
        connection.starttls()

        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='ytra1001@hotmail.com', msg=f"Subject: Quote of Day!\n\n{day_quote}")
