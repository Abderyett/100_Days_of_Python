import smtplib

my_email = 'abderyetttesting@hotmail.com'
password = '123456789@()'

connection = smtplib.SMTP('smtp-mail.outlook.com')
connection.starttls()

connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email,
                    to_addrs='ytra1001@hotmail.com', msg="Hello there!")
connection.close()
