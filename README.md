# ISS Notification Script

This Python script periodically checks if the International Space Station (ISS) is nearby and if it's nighttime at a specified location. If both conditions are met, it sends an email notification.

## Description

The script uses two main functions:

1. `iss_incoming()`: Retrieves the current location of the ISS from the Open Notify API and checks if it's within a specified range of latitude and longitude coordinates.

2. `night_time()`: Determines if it's nighttime at the specified location using the Sunrise-Sunset API.

If the ISS is nearby and it's nighttime, the script sends an email notification using SMTP.

## Configuration

Before running the script, ensure the following:

- Set the latitude and longitude coordinates (`MY_LAT` and `MY_LNG`) of the location you want to monitor.
- Configure your email address (`MY_MAIL`) and password (`PASSWORD`) for sending email notifications.

## Usage

1. Clone this repository:

         git clone https://github.com/godwinolekanma/ISS-TRACKER.git
2. Modify the script with your latitude, longitude, email credentials, and any other necessary changes.

3. Run the script:

## APIs Used
- Open Notify API: Used to retrieve the current location of the ISS.
- Sunrise-Sunset API: Used to determine if it's nighttime at the specified location.

## Notes
- use python anywhere to run the script at a particular time( night preferably for visibility ) https://www.pythonanywhere.com/
- test this using the current location of the ISS lon and lat
- use an email app password or lower email security if email not sent when testing

