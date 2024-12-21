#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from tkinter import Tk
import sys

sys.path.append('../src')
from idz3 import ResizableTextApp


class TestResizableTextApp(unittest.TestCase):
    def setUp(self):
        # Создаем корневое окно и экземпляр приложения
        self.root = Tk()
        self.app = ResizableTextApp(self.root)

    def tearDown(self):
        # Закрываем окно после тестов
        self.root.destroy()

    def test_initial_sizes(self):
        """Тестируем начальные размеры текстового поля."""
        width = int(self.app.text_area["width"])
        height = int(self.app.text_area["height"])
        self.assertEqual(width, 25)
        self.assertEqual(height, 12)

    def test_resize_text(self):
        """Тестируем изменение размеров текстового поля."""
        # Устанавливаем новые значения в поля ввода
        self.app.width_entry.delete(0, "end")
        self.app.width_entry.insert(0, "30")
        self.app.height_entry.delete(0, "end")
        self.app.height_entry.insert(0, "15")

        # Вызываем метод для изменения размеров
        self.app.resize_text()

        # Проверяем, что размеры текстового поля изменились
        width = int(self.app.text_area["width"])
        height = int(self.app.text_area["height"])
        self.assertEqual(width, 30)
        self.assertEqual(height, 15)

    def test_invalid_resize(self):
        """Тестируем ввод некорректных данных."""
        # Устанавливаем некорректные значения в поля ввода
        self.app.width_entry.delete(0, "end")
        self.app.width_entry.insert(0, "invalid")
        self.app.height_entry.delete(0, "end")
        self.app.height_entry.insert(0, "invalid")

        # Вызываем метод для изменения размеров
        self.app.resize_text()

        # Проверяем, что размеры текстового поля остались прежними
        width = int(self.app.text_area["width"])
        height = int(self.app.text_area["height"])
        self.assertEqual(width, 25)
        self.assertEqual(height, 12)

if __name__ == "__main__":
    unittest.main()