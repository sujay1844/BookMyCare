from tkinter import Button, Frame
from tkinter import Frame, Tk

def create_buttons(frame:Frame) -> list:
    btns = [Button() for _ in range(12)]

    btns[0] = Button(frame, text=0, command=lambda:inp(0))
    btns[1] = Button(frame, text=1, command=lambda:inp(1))
    btns[2] = Button(frame, text=2, command=lambda:inp(2))
    btns[3] = Button(frame, text=3, command=lambda:inp(3))
    btns[4] = Button(frame, text=4, command=lambda:inp(4))
    btns[5] = Button(frame, text=5, command=lambda:inp(5))
    btns[6] = Button(frame, text=6, command=lambda:inp(6))
    btns[7] = Button(frame, text=7, command=lambda:inp(7))
    btns[8] = Button(frame, text=8, command=lambda:inp(8))
    btns[9] = Button(frame, text=9, command=lambda:inp(9))
    btns[10] = Button(frame, text="*", command=lambda:inp("*"))
    btns[11] = Button(frame, text="#", command=lambda:inp("#"))

    for btn in btns:
        btn.configure(font=("Calibri", 40), padx=10, pady=10, width=5, height=3)

    btns[0].grid(row=3, column=1)
    btns[1].grid(row=0, column=0)
    btns[2].grid(row=0, column=1)
    btns[3].grid(row=0, column=2)
    btns[4].grid(row=1, column=0)
    btns[5].grid(row=1, column=1)
    btns[6].grid(row=1, column=2)
    btns[7].grid(row=2, column=0)
    btns[8].grid(row=2, column=1)
    btns[9].grid(row=2, column=2)
    btns[10].grid(row=3, column=0)
    btns[11].grid(row=3, column=2)
    return btns

def inp(x):
    with open('inp.txt', 'w') as file:
        file.write(str(x))

root = Tk()
frame = Frame(root)
btns = create_buttons(frame)
frame.pack()
root.mainloop()
