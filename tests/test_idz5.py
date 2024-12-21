#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import MagicMock
import sys

sys.path.append('../src')
from idz5 import Canvas, BallMover


# Подключаем код с классом BallMover
class BallMoverTest(unittest.TestCase):
    def setUp(self):
        # Создаем фиктивный объект Canvas
        self.canvas = MagicMock(spec=Canvas)
        # Настраиваем начальные координаты круга
        self.ball = "ball_id"
        self.canvas.coords.return_value = [100, 40, 140, 80]

        # Создаем экземпляр BallMover
        self.mover = BallMover(self.canvas, self.ball)

    def test_set_target(self):
        # Устанавливаем целевую позицию через событие
        event = MagicMock()
        event.x, event.y = 200, 100
        self.mover.set_target(event)

        # Проверяем, что target_x и target_y установлены правильно
        self.assertEqual(self.mover.target_x, 200)
        self.assertEqual(self.mover.target_y, 100)

    def test_move_to_target(self):
        # Устанавливаем целевую позицию
        self.mover.target_x = 200
        self.mover.target_y = 100

        # Вызываем метод move_to_target
        self.mover.move_to_target()

        # Проверяем, что были вызваны методы для движения круга
        self.canvas.move.assert_called_with(self.ball, 1, 1)  # Движение вправо и вниз
        self.canvas.after.assert_called_with(10, self.mover.move_to_target)

    def test_no_movement_if_at_target(self):
        # Устанавливаем текущие координаты круга в целевую позицию
        self.canvas.coords.return_value = [190, 90, 210, 110]  # Центр круга совпадает с target
        self.mover.target_x = 200
        self.mover.target_y = 100

        # Вызываем метод move_to_target
        self.mover.move_to_target()

        # Проверяем, что движение не было вызвано
        self.canvas.move.assert_not_called()
        self.canvas.after.assert_not_called()


if __name__ == "__main__":
    unittest.main()