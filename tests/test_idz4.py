#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import tkinter as tk
import sys

sys.path.append('../src')
from idz4 import draw_scene


class TestDrawScene(unittest.TestCase):
    def setUp(self):
        """Создаем canvas для тестирования."""
        self.root = tk.Tk()
        self.canvas_width = 400
        self.canvas_height = 300
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

    def tearDown(self):
        """Закрываем окно после теста."""
        self.root.destroy()

    def test_draw_scene(self):
        """Тестируем функцию draw_scene."""
        draw_scene(self.canvas, self.canvas_width, self.canvas_height)

        # Проверяем количество объектов на canvas
        items = self.canvas.find_all()
        self.assertGreater(len(items), 0, "На canvas не добавлены графические элементы.")

        # Проверяем наличие основных объектов
        rectangles = [item for item in items if self.canvas.type(item) == "rectangle"]
        polygons = [item for item in items if self.canvas.type(item) == "polygon"]
        ovals = [item for item in items if self.canvas.type(item) == "oval"]
        arcs = [item for item in items if self.canvas.type(item) == "arc"]

        self.assertGreaterEqual(len(rectangles), 2, "Ожидалось как минимум 2 прямоугольника.")
        self.assertGreaterEqual(len(polygons), 1, "Ожидался как минимум 1 полигон (крыша).")
        self.assertGreaterEqual(len(ovals), 1, "Ожидался как минимум 1 овал (солнце).")
        self.assertGreaterEqual(len(arcs), 1, "Ожидалось как минимум 1 дуга (трава).")


if __name__ == "__main__":
    unittest.main()