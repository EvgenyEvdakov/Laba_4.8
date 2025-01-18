#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# На холсте можно разместить текст. Делается это с помощью метода create_text

from tkinter import *


if __name__ == "__main__":
    root = Tk()

    c = Canvas(root, width=200, height=200, bg="white")
    c.pack()
    c.create_text(100, 100, text="Hello World,\nPython\nand Tk", justify=CENTER, font="Verdana 14")
    c.create_text(200, 200, text="About this", anchor=SE, fill="grey")

    root.mainloop()
