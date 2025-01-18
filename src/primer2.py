#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Метод bind

from tkinter import *


if __name__ == "__main__":

    def changeFont(font):
        l["font"] = font

    root = Tk()
    l = Label(text="Hello World")
    l.pack()
    Button(command=lambda f="Verdana": changeFont(f)).pack()
    Button(command=lambda f="Times": changeFont(f)).pack()
    root.mainloop()
