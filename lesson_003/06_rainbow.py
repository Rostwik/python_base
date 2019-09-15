# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

sd.resolution = (500, 500)
x = 50
x_end = 350

for color_is in rainbow_colors:
    s_point = sd.get_point(x, 50)
    e_point = sd.get_point(x_end, 450)
    sd.line(start_point=s_point, end_point=e_point, color=color_is, width=4)
    x += 5
    x_end += 5

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

s_point = sd.get_point(600, -50)
radius = 400
for color_is in rainbow_colors:
    sd.circle(center_position=s_point, radius=radius, color=color_is, width=20)
    radius += 21

sd.pause()
