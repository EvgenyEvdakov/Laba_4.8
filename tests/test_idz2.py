#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unittest
from tkinter import Tk


sys.path.append("../src")
from idz2 import TextToListApp


class TestTextToListApp(unittest.TestCase):
    def setUp(self):
        # Создаем экземпляр приложения
        self.root = Tk()
        self.app = TextToListApp(self.root)

    def tearDown(self):
        # Закрываем окно после тестов
        self.root.destroy()

    def test_add_to_list(self):
        """Тестируем добавление текста из Entry в Listbox"""
        # Устанавливаем текст в Entry
        self.app.text_entry.insert(0, "Тестовая строка")

        # Имитируем нажатие клавиши Enter
        self.app.add_to_list()

        # Проверяем, что текст добавлен в Listbox
        self.assertEqual(self.app.text_list.size(), 1)
        self.assertEqual(self.app.text_list.get(0), "Тестовая строка")

        # Проверяем, что поле Entry очищено
        self.assertEqual(self.app.text_entry.get(), "")

    def test_add_empty_text(self):
        """Тестируем, что пустая строка не добавляется"""
        # Оставляем поле Entry пустым
        self.app.text_entry.delete(0, "end")

        # Имитируем нажатие клавиши Enter
        self.app.add_to_list()

        # Проверяем, что Listbox остался пустым
        self.assertEqual(self.app.text_list.size(), 0)

    def test_copy_to_entry(self):
        """Тестируем копирование текста из Listbox в Entry"""
        # Добавляем элемент в Listbox
        self.app.text_list.insert(0, "Тестовая строка")

        # Выбираем элемент
        self.app.text_list.select_set(0)

        # Имитируем двойной клик
        self.app.copy_to_entry()

        # Проверяем, что текст скопировался в Entry
        self.assertEqual(self.app.text_entry.get(), "Тестовая строка")

    def test_no_selection_copy(self):
        """Тестируем, что ничего не происходит, если нет выделенного элемента"""
        # Имитируем двойной клик при пустом выборе
        self.app.copy_to_entry()

        # Проверяем, что поле Entry остается пустым
        self.assertEqual(self.app.text_entry.get(), "")


if __name__ == "__main__":
    unittest.main()
