from tkinter import *

root = Tk()

# Creating a Label widger=t
myLabel1 = Label(root, text="Hello World!").grid(row = 0, column = 0)
myLabel2 = Label(root, text="My name is Sahil").grid(row = 1, column = 5)

# myLabel1.grid(row = 0, column = 0)
# myLabel2.grid(row = 1, column = 5)


root.mainloop()