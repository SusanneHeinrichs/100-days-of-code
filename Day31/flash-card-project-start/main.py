from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pd.read_csv("/Users/suse/dev/100-days-of-code/Day31/flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("/Users/suse/dev/100-days-of-code/Day31/flash-card-project-start/data/french_words.csv")
finally: 
    to_learn = df.to_dict(orient = "records")
current_card = {} 

# ---------------------------- Generate random word ------------------------------- #
def show_new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"], fill = "black")
    canvas.itemconfig(card_background, image = card_front_img)
    flip_timer = window.after(3000, func =  flip_card)
    
def delete_learned_word():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("/Users/suse/dev/100-days-of-code/Day31/flash-card-project-start/data/words_to_learn.csv", index = False)
    show_new_card()

def flip_card():
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill  = "white")
    canvas.itemconfig(card_background, image = card_back_img)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func =  flip_card)

canvas = Canvas(width = 800, height = 526)
card_front_img = PhotoImage(file = "/Users/suse/dev/100-days-of-code/Day31/flash-card-project-start/images/card_front.png")
card_front = canvas.create_image(400,263, image = card_front_img)
card_back_img = PhotoImage(file = "/Users/suse/dev/100-days-of-code/Day31/flash-card-project-start/images/card_back.png")
card_background = canvas.create_image(400,263, image = card_back_img) 
canvas.config(bg = BACKGROUND_COLOR, highlightthickness= 0)
canvas.grid(row = 0, column = 0, columnspan = 2 )
card_title = canvas.create_text(400,150, text= "French", font = ("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text = "Start", font = ("Ariel", 60, "bold"))


wrong = PhotoImage(file = "/Users/suse/dev/100-days-of-code/Day31/flash-card-project-start/images/wrong.png")
wrong_button = Button(image = wrong, highlightthickness= 0, command=show_new_card)
wrong_button.grid(row = 1, column = 0)
right = PhotoImage(file = "/Users/suse/dev/100-days-of-code/Day31/flash-card-project-start/images/right.png")
right_button = Button(image = right, highlightthickness= 0, command = delete_learned_word)
right_button.grid(row = 1, column = 1)

show_new_card()

window.mainloop()





