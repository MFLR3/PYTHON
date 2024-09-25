import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

SENDER_EMAIL = "placeholder"
SENDER_PASSWORD = "placeholder"
RECIPIENT_EMAIL = "placeholder"

with open('quotes.txt', 'r') as file:
    quotes = file.readlines()

random_quote = random.choice(quotes)

if weekday == 2:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECIPIENT_EMAIL,
            msg=f"Subject:Hello\n\n{random_quote}"
        )
