from tkinter import Button, Frame, Tk
root = Tk()

def hello():
    print("hello")

frame = Frame(root)
frame.pack()
b1 = Button(frame, text="Press me", command=hello)
b1.pack()

root.mainloop()
