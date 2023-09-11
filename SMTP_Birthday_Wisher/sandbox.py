# Send your friend a email at their birthday by python.
# import smtplib


# my_email = "sherryuuer@gmail.com"
# password = "hnghdcvtfewaxnuz"  # app password

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()  # Make the connectiong secure.
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=my_email,
#                         msg="Subject:hello\n\nThis is the body of the email."
#                         )
   
# import datetime as dt


# now = dt.datetime.now()
# print(now)
# print(type(now))
# print(now.year)
# print(type(now.year))
# print(now.month)
# print(type(now.month))
# print(now.weekday())  # don not forget the () --day of week,monday got 0
# print(type(now.weekday()))

# date_of_birth = dt.datetime(year=2000, month=1, day=1)  # they are all int, so can not use 01
# print(date_of_birth)
