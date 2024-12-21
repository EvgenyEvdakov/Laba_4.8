#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В программе создается холст. На нем с помощью метода create_line рисуются отрезки.
# Сначала указываются координаты начала (x1, y1), затем – конца (x2, y2).

from tkinter import *

if __name__ == "__main__":
    root = Tk()

    c = Canvas(root, width=200, height=200, bg='white')
    c.pack()
    c.create_line(10, 10, 190, 50)

    c.create_line(100, 180, 100, 60, fill='green',
                    width=5, arrow=LAST, dash=(10,2),
                    activefill='lightgreen',
                    arrowshape="10 20 10")

    root.mainloop()