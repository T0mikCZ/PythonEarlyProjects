import tkinter as tk
from PIL import ImageTk, Image
#Main Window Config

root = tk.Tk()
root.title("ImageTest")
root.iconbitmap("C:/python/Matika/dio.ico")

frame = tk.LabelFrame(root, text="This is my Frame...", padx=5, pady=5)
frame.pack(padx=10, pady=10)

button = tk.Button(frame, text="Button")
button.pack()

button2 = tk.Button(frame, text="Button")
button2.pack()

button3 = tk.Button(frame, text="Button")
button3.pack()

root.mainloop()