import datetime as dt
import pandas as pd
import random
import smtplib

today = dt.datetime.now()
today_tuple = (today.month, today.day)

MY_EMAIL = "testingemail@gmail.com"
MY_PASSWORD = "1234"

data = pd.read_csv("birthdays.csv")
birthday_dict = {
    (data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()
}


if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person['email'],
            msg= f"Subject: Happy Birthday! \n\n{contents}"
        )