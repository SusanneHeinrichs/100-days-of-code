from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Miles to km converter")
window.minsize(width=500, height=200)
window.config(padx = 25, pady = 30)

#Entry
miles = Entry(width = 30)
miles.insert(END, string = "0")
print(miles.get())
miles.grid(column = 1, row = 0)

#Labels
label_miles = Label(text="Miles")
label_miles.grid(column = 2, row= 0)
label_km = Label(text = "Km")
label_km.grid(column = 2, row = 1)
label_equal = Label(text = "is equal to:")
label_equal.grid(column =0, row = 1)
label_number = Label(text = "0")
label_number.grid(column = 1, row = 1)

#Buttons
def calculate():
    result = int(miles.get()) *1.609
    label_number.config(text = str(result))

#calls action() when pressed
button = Button(text="Calculate", command=calculate)
#button.pack()
button.grid(column = 1, row = 2)

window.mainloop()
