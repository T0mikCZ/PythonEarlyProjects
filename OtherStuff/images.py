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

imageList = [sharingan1, sharingan2, sharingan3, sharinganMS, sharinganEMS, rinnegan]

#Defining image labels

myImageLabel = tk.Label(image=sharingan1)
#mySharingan2Label = tk.Label(image=sharingan2)
#mySharingan3Label = tk.Label(image=sharingan3)

#mySharinganMSLabel = tk.Label(image=sharinganMS)
#mySharinganEMSLabel = tk.Label(image=sharinganEMS)

#myRinneganLabel = tk.Label(image=rinnegan)
#Displaying them

myImageLabel.grid(row=0,column=0, columnspan=3)
#mySharingan2Label.grid(row=0,column=1)
#mySharingan3Label.grid(row=0,column=2)

#mySharinganMSLabel.grid(row=0,column=3)
#mySharinganEMSLabel.grid(row=0,column=4)

#myRinneganLabel.grid(row=0, column=5)

def forward(imageIndex):
    global myImageLabel
    global buttonForward
    global buttonBack

    myImageLabel.grid_forget()
    myImageLabel = tk.Label(image=imageList[imageIndex-1])

    buttonForward = tk.Button(root, text=">>>", command=lambda: forward(imageIndex+1))
    buttonBack = tk.Button(root, text="<<<", command= lambda: back(imageIndex-1))

    if imageIndex == 6:
       buttonForward = tk.Button(root, text=">>>", state=tk.DISABLED) 

    myImageLabel.grid(row=0,column=0, columnspan=3)
    buttonBack.grid(row=1, column=0)
    buttonForward.grid(row=1, column=2) 

def back(imageIndex):
    global myImageLabel
    global buttonForward
    global buttonBack

    myImageLabel.grid_forget()

    myImageLabel = tk.Label(image=imageList[imageIndex-1])
    buttonForward = tk.Button(root, text=">>>", command=lambda: forward(imageIndex+1))
    buttonBack = tk.Button(root, text="<<<", command= lambda: back(imageIndex-1))

    if imageIndex == 1:
       buttonBack = tk.Button(root, text=">>>", state=tk.DISABLED) 

    myImageLabel.grid(row=0,column=0, columnspan=3)
    buttonBack.grid(row=1, column=0)
    buttonForward.grid(row=1, column=2) 

buttonBack = tk.Button(root, text="<<<", command=back, state=tk.DISABLED)
buttonExit = tk.Button(root, text="Exit Program", command=root.quit)
buttonForward = tk.Button(root, text=">>>", command = lambda: forward(2))

buttonBack.grid(row=1, column=0)
buttonExit.grid(row=1, column=1)
buttonForward.grid(row=1, column=2)
root.mainloop()