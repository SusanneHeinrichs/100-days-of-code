from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
#label.pack()
label.grid(column = 0, row= 0)

#Buttons
def action():
    print("Do something")
    label.config(text = "Something was done.")

#calls action() when pressed
button = Button(text="Click Me", command=action)
#button.pack()
button.grid(column = 1, row = 1)

button2 = Button(text = 'I am new here')
button2.grid(column =2, row = 0)

#Entries
entry = Entry(width=30)
#Gets text in entry
print(entry.get())
entry.grid(column = 3, row = 2)



window.mainloop()
