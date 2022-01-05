##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas as pd
import random
import smtplib

birthdays = pd.read_csv("/Users/suse/dev/100-days-of-code/Day32/birthday-wisher-extrahard-start/birthdays.csv")
print(birthdays)
today = dt.datetime.now()
month, day = today.month, today.day 
for index, row in birthdays.iterrows():
    if (row['month'] == month and row['day'] == day):
        letter_no = random.randint(1,3)

        with open(f'/Users/suse/dev/100-days-of-code/Day32/birthday-wisher-extrahard-start/letter_templates/letter_{letter_no}.txt', 'r') as file :
            letter = file.read()
        letter = letter.replace('[NAME]',row['name'])

        my_email = "susanne100DaysOfCode@gmail.com"
        passw = "XXXXXXX"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = my_email, password = passw )
            connection.sendmail(from_addr= my_email, to_addrs = row["email"], msg = f"Subject: Happy Birthday <3 \n\n{letter}")






