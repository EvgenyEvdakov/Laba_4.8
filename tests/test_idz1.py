#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unittest
from tkinter import Tk


sys.path.append("../src")
from idz1 import ProductTransferApp


class TestProductTransferApp(unittest.TestCase):
    def setUp(self):
        # Создаем экземпляр приложения
        self.root = Tk()
        self.app = ProductTransferApp(self.root)

    def tearDown(self):
        # Закрываем окно после тестов
        self.root.destroy()

    def test_initial_product_list(self):
        # Проверяем, что изначально список продуктов заполнен корректно
        expected_products = ["Хлеб", "Молоко", "Сыр", "Масло", "Кофе", "Чай", "Шоколад"]
        actual_products = [self.app.product_list.get(i) for i in range(self.app.product_list.size())]
        self.assertEqual(expected_products, actual_products)

    def test_add_to_cart(self):
        # Выбираем элемент и перемещаем его в корзину
        self.app.product_list.select_set(0)  # Выбираем "Хлеб"
        self.app.add_to_cart()

        # Проверяем, что товар переместился в корзину
        self.assertEqual(self.app.cart_list.get(0), "Хлеб")
        self.assertEqual(self.app.product_list.size(), 6)  # Количество элементов уменьшилось

    def test_remove_from_cart(self):
        # Добавляем элемент в корзину
        self.app.product_list.select_set(0)  # Выбираем "Хлеб"
        self.app.add_to_cart()

        # Теперь удаляем его из корзины
        self.app.cart_list.select_set(0)  # Выбираем "Хлеб" в корзине
        self.app.remove_from_cart()

        # Проверяем, что товар вернулся в список продуктов
        self.assertEqual(self.app.product_list.size(), 7)
        self.assertEqual(self.app.product_list.get(self.app.product_list.size() - 1), "Хлеб")
        self.assertEqual(self.app.cart_list.size(), 0)  # Корзина пуста


if __name__ == "__main__":
    unittest.main()
