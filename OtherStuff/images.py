import tkinter as tk
from PIL import ImageTk, Image
#Main Window Config

root = tk.Tk()
root.title("ImageTest")
root.iconbitmap("C:/python/Matika/dio.ico")

#Defining images as variables

sharingan1 = ImageTk.PhotoImage(Image.open("C:/python/OtherStuff/Images/Sharingan1Tomoe.png"))
sharingan2 = ImageTk.PhotoImage(Image.open("C:/python/OtherStuff/Images/Sharingan2Tomoe.png"))
sharingan3 = ImageTk.PhotoImage(Image.open("C:/python/OtherStuff/Images/Sharingan3Tomoe.png"))

sharinganMS = ImageTk.PhotoImage(Image.open("C:/python/OtherStuff/Images/MadaraMangekyo.png"))
sharinganEMS = ImageTk.PhotoImage(Image.open("C:/python/OtherStuff/Images/MadaraEternalMangekyo.png"))

rinnegan = ImageTk.PhotoImage(Image.open("C:/python/OtherStuff/Images/Rinnegan.png"))
#Defining image labels

mySharingan1Label = tk.Label(image=sharingan1)
mySharingan2Label = tk.Label(image=sharingan2)
mySharingan3Label = tk.Label(image=sharingan3)

mySharinganMSLabel = tk.Label(image=sharinganMS)
mySharinganEMSLabel = tk.Label(image=sharinganEMS)

myRinneganLabel = tk.Label(image=rinnegan)
#Displaying them

mySharingan1Label.grid(row=0,column=0)
mySharingan2Label.grid(row=0,column=1)
mySharingan3Label.grid(row=0,column=2)

mySharinganMSLabel.grid(row=0,column=3)
mySharinganEMSLabel.grid(row=0,column=4)

myRinneganLabel.grid(row=0, column=5)

root.mainloop()