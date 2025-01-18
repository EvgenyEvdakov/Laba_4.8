#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: в данной программе создается анимация круга, который движется от левой
# границы холста до правой. Выражение c.coords(ball) возвращает список текущих координат объекта (в данном
# случае это ball). Третий элемент списка соответствует его второй координате x.
# Метод after вызывает функцию, переданную вторым аргументом, через количество
# миллисекунд, указанных первым аргументом.
# Необходимо запрограммировать постепенное движение фигуры в ту точку холста, где пользователь
# кликает левой кнопкой мыши. Координаты события хранятся в его атрибутах x и y (event.x, event.y).


from tkinter import Canvas, Tk


class BallMover:
    def __init__(self, canvas, ball):
        self.canvas = canvas
        self.ball = ball
        self.target_x = None
        self.target_y = None

    def move_to_target(self):
        if self.target_x is not None and self.target_y is not None:
            # Получаем текущие координаты круга
            x1, y1, x2, y2 = self.canvas.coords(self.ball)
            ball_center_x = (x1 + x2) / 2
            ball_center_y = (y1 + y2) / 2

            # Вычисляем смещение
            dx = 1 if ball_center_x < self.target_x else -1 if ball_center_x > self.target_x else 0
            dy = 1 if ball_center_y < self.target_y else -1 if ball_center_y > self.target_y else 0

            # Двигаем круг, если он не достиг цели
            if dx != 0 or dy != 0:
                self.canvas.move(self.ball, dx, dy)
                self.canvas.after(10, self.move_to_target)

    def set_target(self, event):
        """Устанавливает новую цель для движения круга."""
        self.target_x = event.x
        self.target_y = event.y
        self.move_to_target()


def main():
    root = Tk()
    root.title("Ball Movement")
    canvas = Canvas(root, width=300, height=200, bg="white")
    canvas.pack()

    # Создаем круг
    ball = canvas.create_oval(100, 40, 140, 80, fill="green")

    # Создаем объект BallMover
    ball_mover = BallMover(canvas, ball)

    # Привязываем обработчик клика мыши
    canvas.bind("<Button-1>", ball_mover.set_target)

    root.mainloop()


if __name__ == "__main__":
    main()
