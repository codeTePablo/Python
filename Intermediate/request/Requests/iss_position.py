import requests
from datetime import datetime
import time
import smtplib

#  Create load env
MY_EMAIL = "jopsan63@gmail.com"
MY_PASSWORD = ""

MY_LAT = 19.432608
MY_LONG = -99.133209


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    my_position = (MY_LAT, MY_LONG)
    iss_position = (iss_latitude, iss_longitude)
    # print(f"iss_position: {iss_position}")
    # print(f"my_position: {my_position}")
    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True
    else:
        raise Exception("no yet")


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)  #  wait 60 seconds to reiniciate code
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp@gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky.",
        )
