import smtplib
import datetime as dt
import random

today = dt.datetime.now().weekday()
print(today)
if (today == 2):
    with open ("/Users/suse/dev/100-days-of-code/Day32/Birthday Wisher (Day 32) start/quotes.txt") as file:
        lines = file.readlines()
    random_quote = random.choice(lines)

    print(random_quote)
    my_email = "susanne100DaysOfCode@gmail.com"
    passw = "gagxaw-gasnit-8Foxma"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = "susanne100DaysOfCode@gmail.com", password = passw )
        connection.sendmail(from_addr= my_email, to_addrs = "susanne100DaysOfCode@yahoo.com", msg = f"Subject: Here is an inspirational quote for you\n\n{random_quote}")


