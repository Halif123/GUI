

# Graphic user interface
# Tkinter
#textbutton - to receive information
#to arrange we have pack,grid and place :place:it uses y axis and x axis :Grid:it works in row and columns





from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("ABATI")

root.geometry("900x900")
def fifi():
    w1=g1.get()
    b2=g2.get()
    if w1=="" and b2=="":
       messagebox.showerror("ERROR","inValid")
    else:
        std = "welcome" + w1
        messagebox.showinfo("Welcome","valid")
g1 = StringVar()
g2= StringVar()
r1 = Label(root, text="Username:", fg="blue").grid(row=0,column=0)
r2 = Label(root, text="Password:", fg="green").grid(row=1,column=0)
t1 = Entry(root, textvariable=g1)
t2 = Entry(root, textvariable=g2)
t1.grid(row=0, column=1)
t2.grid(row=1, column=1)
f1 = Button(root,text="Enter",bg="red",command=fifi).place(x=30,y=50)
f2 = Button(root,text="Reset",bg="red").place(x=80,y=50)
#g1= Message(root,text="error",bg ="green",).grid(pady=67)

root.mainloop()