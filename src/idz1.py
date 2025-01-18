#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: напишите программу, состоящую из двух списков Listbox. В первом будет,
# например, перечень товаров, заданный программно. Второй изначально пуст, пусть это
# будет перечень покупок. При клике на одну кнопку товар должен переходить из одного
# списка в другой. При клике на вторую кнопку – возвращаться (человек передумал покупать).
# Предусмотрите возможность множественного выбора элементов списка и их перемещения.

import tkinter as tk
from tkinter import MULTIPLE, Button, Listbox


class ProductTransferApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Перечень товаров")

        self.create_widgets()
        self.populate_product_list()

    def create_widgets(self):
        # Список товаров
        self.product_list = Listbox(self.root, selectmode=MULTIPLE, width=30, height=15)
        self.product_list.grid(row=0, column=0, padx=10, pady=10)

        # Кнопки управления
        self.add_button = Button(self.root, text="Добавить →", command=self.add_to_cart)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.remove_button = Button(self.root, text="← Удалить", command=self.remove_from_cart)
        self.remove_button.grid(row=1, column=1, padx=5, pady=5)

        # Список покупок
        self.cart_list = Listbox(self.root, selectmode=MULTIPLE, width=30, height=15)
        self.cart_list.grid(row=0, column=2, padx=10, pady=10)

    def populate_product_list(self):
        # Предустановленный список товаров
        products = ["Хлеб", "Молоко", "Сыр", "Масло", "Кофе", "Чай", "Шоколад"]
        for product in products:
            self.product_list.insert(tk.END, product)

    def add_to_cart(self):
        selected_items = self.product_list.curselection()
        for index in reversed(selected_items):  # Обратный порядок, чтобы индексы оставались корректными
            item = self.product_list.get(index)
            self.cart_list.insert(tk.END, item)
            self.product_list.delete(index)

    def remove_from_cart(self):
        selected_items = self.cart_list.curselection()
        for index in reversed(selected_items):  # Обратный порядок, чтобы индексы оставались корректными
            item = self.cart_list.get(index)
            self.product_list.insert(tk.END, item)
            self.cart_list.delete(index)


if __name__ == "__main__":
    root = tk.Tk()
    app = ProductTransferApp(root)
    root.mainloop()
