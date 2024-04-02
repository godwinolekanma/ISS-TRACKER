"""
find latitude and longitude location on the map using:
www.latlong.net/geo-tools
"""

# used to make API requests
import requests
import os
from datetime import datetime
import time
import smtplib

MY_MAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
MY_LAT = float(os.environ.get("MY_LAT"))
MY_LNG = float(os.environ.get("MY_LNG"))


def iss_incoming():
    # API to get ISS location
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    # gives the latitude and longitude for the ISS
    latitude = float(response.json()["iss_position"]["latitude"])
    longitude = float(response.json()["iss_position"]["longitude"])
    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LNG - 5 <= longitude <= MY_LNG + 5:
        return True


def night_time():
    now = datetime.now()
    current_hour = now.hour
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
        "tzid": "America/Chicago"
    }
    # Api to check nighttime in my location
    response = requests.get("https://api.sunrise-sunset.org/json", parameters)
    response.raise_for_status()
    sunrise_hour = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])
    if sunset_hour <= current_hour or current_hour <= sunrise_hour:
        return True


def send_email():
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=MY_MAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_MAIL,
        to_addrs=MY_MAIL,
        msg="Subject: ISS Incoming\n\nLook Up!"
    )


while True:
    # run this script every 60 seconds
    time.sleep(60)
    if iss_incoming() and night_time():
        send_email()
