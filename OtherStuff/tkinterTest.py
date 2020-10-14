import tkinter as tk

root = tk.Tk()

myLabel1 = tk.Label(root, text="Hello World")
myLabel2 = tk.Label(root, text="My name is Tomik")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)

root.mainloop()