#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Виджет Listbox

from tkinter import *

def add_item():
    box.insert(END, entry.get())
    entry.delete(0, END)


def del_list():
    select = list(box.curselection())
    select.reverse()
    for i in select:
        box.delete(i)


def save_list():
    with open('list000.txt', 'w') as f:
        f.writelines("\n".join(box.get(0, END)))


if __name__ == "__main__":
    root = Tk()

    box = Listbox(root, selectmode=EXTENDED)
    box.pack(side=LEFT)

    scroll = Scrollbar(root, command=box.yview)
    scroll.pack(side=LEFT, fill=Y)
    box.config(yscrollcommand=scroll.set)

    f = Frame(root)
    f.pack(side=LEFT, padx=10)

    entry = Entry(f)
    entry.pack(anchor=N)

    Button(f, text="Add", command=add_item).pack(fill=X)
    Button(f, text="Delete", command=del_list).pack(fill=X)
    Button(f, text="Save", command=save_list).pack(fill=X)

    root.mainloop()