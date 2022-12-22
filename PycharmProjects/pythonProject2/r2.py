from tkinter import *
from tkinter import ttk
root = Tk()
root.title("shock")
root.geometry("500x500")
l1 = Label(root, text="Gender").grid(column=0, row=0)
va = StringVar()
#checkbutton-It's use for selecting multiple options
#Radio button-it's use for choosing on option out of multiple choice

wad1 = Radiobutton(root, text="female", value="Female", variable=va).grid(column=1, row=0)
wad2 = Radiobutton(root, text="male", value="male", variable=va).grid(column=2, row=0)
R2 = Label(root, text="Education").grid(row=0, column=0)
che1 = Checkbutton(root, text="SSce", onvalue=1, offvalue=0).grid(row=2, column=0)
ma1 = Checkbutton(root, text="MSC").grid(row=3, column=0)
#listbox - to create a list
L6 = Label(root, text="Food Options").grid(row=4, column=0)
l7 = Listbox(root)
l7.insert(1, "Amala")
l7.insert(2, "Pizza")
l7.insert(3, "Chicken burger")
l7.grid(row=4, column=0)
fruits = ("mango", "cherry", "pine-apple")
box = ttk.Combobox(root, values=fruits).grid(row=8, column=0)
#assignment-build different form Of object
mainloop()
