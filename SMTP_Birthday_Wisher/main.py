# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
import datetime as dt
import pandas as pd
# import smtplib
import random

MY_EMAIL = "sherryuuer@gmail.com"
PASSWORD = "hnghdcvtfewaxnuz"

now = dt.datetime.now()  # datetime to string.
today = f"{now.month}-{now.day}"

# Name list.
names = pd.read_csv("SMTP_Birthday_Wisher/birthdays.csv")
name_list = names.to_dict(orient="records")

# Check if it is today.
for name in name_list:
    month = name["month"]
    day = name["day"]  
    to_email = name["email"]
    birthday = f"{month}-{day}"
    if birthday == today:
        # send the email
        with open(f"SMTP_Birthday_Wisher/letter_templates/letter_{random.randint(1,3)}.txt") as f:
            contents = f.read()
            contents = contents.replace("[NAME]", name["name"])
        print(contents)
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=MY_EMAIL, password=PASSWORD)
        #     connection.sendmail(from_addr=MY_EMAIL,
        #                         to_addrs=to_email,
        #                         msg=f"Subject:Happy Birthday!\n\n{contents}."
        #                         )


# End code from Angla↓

# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


# from datetime import datetime
# import pandas
# import random
# import smtplib

# MY_EMAIL = "YOUR EMAIL"
# MY_PASSWORD = "YOUR PASSWORD"

# today = datetime.now()
# today_tuple = (today.month, today.day)

# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])

#     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )
