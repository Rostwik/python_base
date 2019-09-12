# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

point = sd.get_point(200, 200)

for i in range(0, 15, 5):
    sd.circle(center_position=point, radius=50 + i, color=(125, 0, 250), width=1)

# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг

def circle_ex(point_cir, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point_cir, radius=radius)

point = sd.get_point(400, 200)
circle_ex(point, 10)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()
