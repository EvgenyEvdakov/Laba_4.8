#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Идентификаторы

from tkinter import *

if __name__ == "__main__":
    root = Tk()
    c = Canvas(width=300, height=300,
               bg='white')
    c.focus_set()
    c.pack()

    ball = c.create_oval(140, 140, 160, 160,
                         fill='green')
    c.bind('<Up>',
          lambda event: c.move(ball, 0, -2))
    c.bind('<Down>',
          lambda event: c.move(ball, 0, 2))
    c.bind('<Left>',
          lambda event: c.move(ball, -2, 0))
    c.bind('<Right>',
      lambda event: c.move(ball, 2, 0))
    root.mainloop()