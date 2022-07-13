import random

import datetime as dt
import smtplib

MY_EMAIL = "testingemail@gmail.com"
MY_PASSWORD = "1234"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.send_message(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )