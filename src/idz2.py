#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: напишите программу по следующему описанию. Нажатие Enter в
# однострочном текстовом поле приводит к перемещению текста из него в список (экземпляр
# Listbox ). При двойном клике ( <Double-Button-1> ) по элементу-строке списка, она должна
# копироваться в текстовое поле.

import tkinter as tk


class TextToListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Текстовое поле и список")

        self.create_widgets()

    def create_widgets(self):
        # Однострочное текстовое поле
        self.text_entry = tk.Entry(self.root, width=40)
        self.text_entry.grid(row=0, column=0, padx=10, pady=10)

        # Привязываем нажатие Enter к методу add_to_list
        self.text_entry.bind("<Return>", self.add_to_list)

        # Список (Listbox)
        self.text_list = tk.Listbox(self.root, width=40, height=15)
        self.text_list.grid(row=1, column=0, padx=10, pady=10)

        # Привязываем двойной клик к методу copy_to_entry
        self.text_list.bind("<Double-Button-1>", self.copy_to_entry)

    def add_to_list(self, event=None):
        """Добавляет текст из текстового поля в список."""
        text = self.text_entry.get().strip()
        if text:  # Проверяем, что текст не пуст
            self.text_list.insert(tk.END, text)
            self.text_entry.delete(0, tk.END)  # Очищаем текстовое поле

    def copy_to_entry(self, event=None):
        """Копирует текст из выбранной строки списка в текстовое поле."""
        selected_index = self.text_list.curselection()
        if selected_index:  # Проверяем, что есть выделенный элемент
            text = self.text_list.get(selected_index)
            self.text_entry.delete(0, tk.END)
            self.text_entry.insert(0, text)


if __name__ == "__main__":
    root = tk.Tk()
    app = TextToListApp(root)
    root.mainloop()
