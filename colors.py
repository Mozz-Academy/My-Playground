import tkinter
from tkinter import *
import random

def change_color():
    bg_color = random.choice(colors)
    canvas = Canvas(root, bg=bg_color, width=600, height=400)
    canvas.grid(row=0, column=0)

root = Tk()
colors = ["aquamarine", "green", "blue", "red", "gray", "yellow", "pink", "orange"]
bg_color = "purple"

canvas = Canvas(root, bg=bg_color, width=600, height=400)
canvas.grid(row=0, column=0)

btn = Button(root, text="RANDOMIZE COLOR", fg="white", bg="black", command=change_color)
btn.grid(row=1, column=0)



root.mainloop()
