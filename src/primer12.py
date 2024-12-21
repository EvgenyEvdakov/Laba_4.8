#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def color(event):
    c.itemconfig('group1', width=3,
                 fill="red")

if __name__ == "__main__":

    root = Tk()
    c = Canvas(width=460, height=150,
               bg='white')
    c.pack()

    oval = c.create_oval(30, 10, 130, 80,
                         tag="group1")
    c.create_line(10, 100, 450, 100,
                    tag="group1")
    c.bind('<Button-3>', color)
    root.mainloop()