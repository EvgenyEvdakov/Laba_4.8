#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: Создайте на холсте изображение. Для создания травы используется цикл.

import tkinter as tk


def draw_scene(canvas, width, height):
    # Небо
    canvas.create_rectangle(0, 0, width, height, fill="white", outline="")

    # Крыша дома
    canvas.create_polygon(
        width // 2 - 70,
        height // 2,  # Левая точка крыши
        width // 2 + 70,
        height // 2,  # Правая точка крыши
        width // 2,
        height // 2 - 100,  # Верхняя точка крыши
        fill="lightblue",
        outline="",
    )

    # Тело дома
    canvas.create_rectangle(
        width // 2 - 50, height // 2, width // 2 + 50, height // 2 + 100, fill="lightblue", outline=""
    )

    # Солнце
    canvas.create_oval(width - 100, 50, width - 50, 100, fill="orange", outline="")

    # Трава
    for x in range(0, width, 15):
        canvas.create_arc(
            x, height - 80, x + 30, height - 20, start=120, extent=60, style=tk.ARC, outline="green", width=2
        )


if __name__ == "__main__":
    # Настройка окна
    root = tk.Tk()
    root.title("Scene with House and Grass")
    canvas_width, canvas_height = 400, 300
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    draw_scene(canvas, canvas_width, canvas_height)

    root.mainloop()
