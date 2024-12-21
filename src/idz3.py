#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: напишите программу по описанию. Размеры многострочного текстового поля
# определяются значениями, введенными в однострочные текстовые поля. Изменение
# размера происходит при нажатии мышью на кнопку, а также при нажатии клавиши Enter.
# Цвет фона экземпляра Text светлосерый (lightgrey), когда поле не в фокусе, и белый,
# когда имеет фокус.
# Событие получения фокуса обозначается как <FocusIn>, потери – как <FocusOut>.
# Для справки: фокус перемещается по виджетам при нажатии Tab, Ctrl+Tab, Shift+Tab, а
# также при клике по ним мышью (к кнопкам последнее не относится).

import tkinter as tk


class ResizableTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Изменяемое поле")

        self.create_widgets()

    def create_widgets(self):
        # Поле для ширины
        self.width_entry = tk.Entry(self.root, width=5)
        self.width_entry.insert(0, "25")  # Устанавливаем значение по умолчанию
        self.width_entry.grid(row=0, column=0, padx=5, pady=5)

        # Поле для высоты
        self.height_entry = tk.Entry(self.root, width=5)
        self.height_entry.insert(0, "12")  # Устанавливаем значение по умолчанию
        self.height_entry.grid(row=1, column=0, padx=5, pady=5)

        # Кнопка для изменения размера
        self.resize_button = tk.Button(self.root, text="Изменить", command=self.resize_text)
        self.resize_button.grid(row=0, column=1, rowspan=2, padx=5, pady=5)

        # Многострочное текстовое поле
        self.text_area = tk.Text(self.root, width=25, height=12, bg="lightgrey")
        self.text_area.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Привязка событий фокуса
        self.text_area.bind("<FocusIn>", self.on_focus_in)
        self.text_area.bind("<FocusOut>", self.on_focus_out)

        # Привязка Enter к изменению размеров
        self.width_entry.bind("<Return>", self.resize_text)
        self.height_entry.bind("<Return>", self.resize_text)

    def resize_text(self, event=None):
        """Изменяет размер текстового поля в соответствии с введенными значениями."""
        try:
            new_width = int(self.width_entry.get())
            new_height = int(self.height_entry.get())
            self.text_area.config(width=new_width, height=new_height)
        except ValueError:
            # Игнорируем ошибки, если введены некорректные данные
            pass

    def on_focus_in(self, event):
        """Меняет цвет фона текстового поля при получении фокуса."""
        self.text_area.config(bg="white")

    def on_focus_out(self, event):
        """Меняет цвет фона текстового поля при потере фокуса."""
        self.text_area.config(bg="lightgrey")


if __name__ == "__main__":
    root = tk.Tk()
    app = ResizableTextApp(root)
    root.mainloop()