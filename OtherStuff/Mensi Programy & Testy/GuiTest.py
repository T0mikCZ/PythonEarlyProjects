import tkinter

window = tkinter.Tk()
window.title("Calculator")

canvas = tkinter.Canvas(window, height = 400, width = 400)
canvas.pack()

frame = tkinter.Frame(window)
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

button = tkinter.Button(frame, text = "Test")
button.pack()

window.mainloop()