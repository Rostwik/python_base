# -*- coding: utf-8 -*-

import simple_draw as sd
from lesson_006.snowfall import create_a_snowflake, move_snowflake, delete_snowflakes, \
    down_snowflakes, draw_color_snowflakes

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

sd.resolution = (1200, 600)
create_a_snowflake(3)

while True:
    draw_color_snowflakes(color=sd.background_color)
    move_snowflake()
    draw_color_snowflakes(color=sd.COLOR_WHITE)
    down_ice = down_snowflakes()

    if down_ice:
        delete_snowflakes(*down_ice)
        create_a_snowflake(len(down_ice))

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
#зачет!