# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# определить функцию рисования треугольника из заданной точки с заданным наклоном

def triangle(point, length, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=1)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=1)
    v3.draw()

    sd.line(start_point=point, end_point=v3.end_point)


def square(point, length, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=1)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=1)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=1)
    v4.draw()

    sd.line(start_point=point, end_point=v4.end_point)


def pentagon(point, length, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=1)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=1)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=1)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=1)
    v5.draw()

    sd.line(start_point=point, end_point=v5.end_point)


def hexagon(point, length, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=1)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=1)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=1)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=1)
    v5.draw()

    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=1)
    v6.draw()

    sd.line(start_point=point, end_point=v6.end_point)


length = 100
point = sd.get_point(100, 100)

triangle(point=point, length=length, angle=30)

length = 100
point = sd.get_point(400, 100)

square(point=point, length=length, angle=30)

length = 100
point = sd.get_point(100, 350)

pentagon(point=point, length=length, angle=30)

length = 100
point = sd.get_point(400, 350)

hexagon(point=point, length=length, angle=30)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
