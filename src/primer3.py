#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# События

from tkinter import *


def b1(event):
    root.title("Левая кнопка мыши")


def b3(event):
    root.title("Правая кнопка мыши")


def move(event):
    x = event.x
    y = event.y
    s = "Движение мышью {}x{}".format(x, y)
    root.title(s)


if __name__ == "__main__":
    root = Tk()
    root.minsize(width=500, height=400)

    root.bind("<Button-1>", b1)
    root.bind("<Button-3>", b3)
    root.bind("<Motion>", move)

    root.mainloop()
