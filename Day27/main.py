from tkinter import *

window = Tk()
window.title('My first GUI Program')
window.minsize(width = 500, height = 300)


#Label
my_label = Label(text = 'Label mem', font = ("Arial", 24, "bold"))
my_label.pack()
 
 #Button

def button_clicked():
    print('I got clicked')

button = Button(text = 'Click me', command = button_clicked)
button.pack()

window.mainloop()

