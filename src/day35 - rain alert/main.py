import requests
import smtplib
import os

LATITUTE = -16.019859
LONGITUDE = -48.014938

api_key = os.environ.get("OWM_API_KEY")
MY_EMAIL = os.environ.get("TEMP_EMAIL")
MY_PASSWORD = os.environ.get("TEMP_PASSWORD")

parameters = {
    "lat": LATITUTE,
    "lon": LONGITUDE,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key,
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", parameters)
response.raise_for_status()

data = response.json()
weather_slice = data['hourly'][:12]

for hour_data in weather_slice:
    condition_code = int(hour_data['weather'][0]['id'])

    if condition_code < 700:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="gabrielleribeiro2010@gmail.com",
                msg="Subject:Bring an umbrella\n\nIt's going to rain today. Bring an umbrella!"
            )
        break