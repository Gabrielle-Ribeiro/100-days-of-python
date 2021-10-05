# Send Motivational Quotes on Mondays via Email

import datetime as dt
import smtplib
import random

current_day_of_week = dt.datetime.now().weekday()

if current_day_of_week == 0:

    with open("quotes.txt", "r") as file:
        quotes = file.readlines()

    today_quote = random.choice(quotes)

    my_email = "youremail@gmail.com"
    my_password = "yourpassword"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="someemail@gmail.com",
                            msg=f"Subject:Motivational Quote\n\n{today_quote}")

