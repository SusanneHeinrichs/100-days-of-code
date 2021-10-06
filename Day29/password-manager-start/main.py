from tkinter import *
import pandas as pd
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_letters = [random.choice(letters) for _ in range(nr_letters)]
password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
password_numbers = [random.choice(symbols) for _ in range(nr_numbers)]

password_list = password_letters + password_symbols + password_numbers 
random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

df  = pd.DataFrame(columns = ['Website', 'Email','Password'])
df.to_csv('password_management.csv', index = False)

def save():
    df = pd.read_csv('password_management.csv')

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = 'Ooops', message = "Please make sure you haven't left empty the website or the password field.")
    else:
        is_okay = messagebox.askokcancel(title = website, message = f"These are the details entered: \n Email: {email} \n Password: {password}. Is it okay to save? ")
        if is_okay:
            df = df.append({'Website': website, 'Email': email, 'Password': password}, ignore_index = True)
            df.to_csv('password_management.csv', index = False)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx = 20, pady= 20)

canvas = Canvas(width = 200, height= 200)
#lock_img = PhotoImage(file = 'logo.png')
#canvas.create_image(100,100, image = lock_img)
#canvas.grid(column = 1, row = 0)

# Labels 
website_label = Label(text = 'Website:')
website_label.grid(column = 0, row = 1)
email_label = Label(text = "Email/ Username:")
email_label.grid( column = 0, row = 2)
password_label = Label(text = "Password:")
password_label. grid(column = 0, row = 3)

#Text entry
website_entry = Entry(width = 38)
website_entry.grid(column = 1, row = 1, columnspan = 2)
website_entry.focus()
email_entry = Entry(width = 38)
email_entry.insert(0, string = "susanneheinrichs1995@gmail.com")
email_entry.grid(column = 1, row = 2, columnspan= 2)
password_entry = Entry(width = 21)
password_entry.grid(column = 1, row = 3)

#Button
generator = Button(text = 'Generate Password')
generator.grid(column = 2, row = 3)
add = Button(text = "Add", width = 36, command = save)
add.grid(column = 1, row = 4, columnspan = 2)

window.mainloop()