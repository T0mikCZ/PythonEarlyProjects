import tkinter as tk
root = tk.Tk()

def calculateOnClick(x,y):
    myLabel = tk.Label(root, text=f"{x}+{y} = {x+y}", fg="red")
    myLabel.pack()

def showNameOnClick(name):
    nameLabel = tk.Label(root, text=f"Your name is {name}")
    nameLabel.grid(column=0, row=4)

myInputBoxX = tk.Entry(root)
#myInputBoxX.pack()

myInputBoxY = tk.Entry(root)
#myInputBoxY.pack()

myNameLabel = tk.Label(root, text="Enter Your name below")
myNameLabel.grid(column=0, row=0)

nameEntry = tk.Entry(root)
nameEntry.grid(column=0, row=1)

myButton = tk.Button(root, text="Click to calculate", padx=5, pady=5, command= lambda: calculateOnClick(int(myInputBoxX.get()),int(myInputBoxY.get())), fg="blue", bg="black")
#myButton.pack()

nameButton = tk.Button(root,text="Click me for showing your name", command= lambda: showNameOnClick(nameEntry.get()))
nameButton.grid(column=0, row=2)

root.mainloop()