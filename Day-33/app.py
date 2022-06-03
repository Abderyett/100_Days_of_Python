import datetime as dt
import requests
import smtplib
import time
MY_LATITUDE = 51.507351
MY_LONGITUDE = -0.127758
my_email = 'abderyetttesting@hotmail.com'
password = '123456789@()'


def is_iss_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')

    # to Raise Error that could occur
    response.raise_for_status()
    data = response.json()
    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])
    position = (iss_latitude, iss_longitude)
    if MY_LATITUDE-5 <= iss_latitude <= MY_LATITUDE+5 and MY_LONGITUDE-5 <= iss_longitude <= MY_LONGITUDE + 5:
        return True


def is_night():
    parameters = {"lat": MY_LATITUDE, "lng": MY_LONGITUDE, "formatted": 0}

    response = requests.get(
        url='https://api.sunrise-sunset.org/json', params=parameters, )
    response.raise_for_status()

    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = dt.datetime.now().hour
    if time_now >= sunset or time_now <= sunset:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead and is_night:
        with smtplib.SMTP('smtp-mail.outlook.com') as connection:
            connection.starttls()

            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs='ytra1001@hotmail.com', msg=f"Subject: Look Up 👆\n\nISS is above you in sky")
