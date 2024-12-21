#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создание прямоугольников методом create_rectangle

from tkinter import *

if __name__ == "__main__":
    root = Tk()

    c = Canvas(root, width=200, height=200, bg='white')
    c.pack()
    c.create_rectangle(10, 10, 190, 60)
    c.create_rectangle(60, 80, 140, 190,
                       fill='yellow',
                       outline='green',
                       width=3,
                       activedash=(5, 4))

    root.mainloop()