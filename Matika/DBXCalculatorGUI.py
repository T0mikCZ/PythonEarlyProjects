import tkinter as tk

root = tk.Tk()

rebirthText = tk.Label(root, text="Rebirths")
rebirthInput = tk.Entry(root)
eventText = tk.Label(root, text="Exp Multiplier")
eventInput = tk.Entry(root)


rebirthText.grid(column=1, row=0)
rebirthInput.grid(column=2, row=0)

eventText.grid(column=1, row=1)
eventInput.grid(column=2, row=1)

root.mainloop()

