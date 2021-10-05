import datetime as dt
import pandas as pd
import random
import smtplib

today = (dt.datetime.now().month, dt.datetime.now().day)

birthdays_data = pd.read_csv("birthdays.csv")
birthdays_dictionary = {(data["month"], data["day"]): data for (index, data) in birthdays_data.iterrows()}

if today in birthdays_dictionary:
    random_number = random.randint(1,3)

    with open(f"letter_templates/letter_{random_number}.txt", "r") as message:
        birthday_message = message.read()
    
    name = birthdays_dictionary[today]['name']
    birthday_message = birthday_message.replace("[NAME]", name)
    
    email = birthdays_dictionary[today]['email']

    my_email = "youremail@gmail.com"
    password = "yourpassword"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=email,
                            msg=f"Subject:Happy Birthday\n\n{birthday_message}")



