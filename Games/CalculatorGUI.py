import tkinter as tk

root = tk.Tk()
root.title("Calculator")

resultEntry = tk.Entry(root, width=40, borderwidth=5)
resultEntry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def buttonClick(number):
    current = resultEntry.get()
    resultEntry.delete(0, tk.END)
    resultEntry.insert(0, str(current) + str(number))
    return

def buttonClear():
    resultEntry.delete(0, tk.END)

def buttonAdd():
    number1 = int(resultEntry.get())
    resultEntry.insert(0, "+")
#Define Buttons

button1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1))
button2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2))
button3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3))
button4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4))
button5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5))
button6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6))
button7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7))
button8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8))
button9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9))
button0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0))
buttonAdd = tk.Button(root, text="+", padx=39, pady=20, command=buttonAdd)
buttonEqual = tk.Button(root, text="=", padx=91, pady=20, command=buttonAdd)
buttonClear = tk.Button(root, text="Clear", padx=79, pady=20, command=buttonClear)
#Put the buttons on the screen

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)

buttonAdd.grid(row=5,column=0)
buttonEqual.grid(row=5,column=1, columnspan=2)
buttonClear.grid(row=4,column=1, columnspan=2)

root.mainloop()