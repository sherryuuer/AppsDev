import datetime as dt
import smtplib
import random


MY_EMAIL = "sherryuuer@gmail.com"
PASSWORD = "hnghdcvtfewaxnuz"


day_of_week = dt.datetime.now().weekday()
if day_of_week == 0:
    with open("SMTP_Birthday_Wisher/quotes.txt") as f:
        data = f.readlines()
        quote = random.choice(data)
    print(quote)   

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Monday QUOTE\n\n{quote}."
                            )
