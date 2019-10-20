# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(50, 1150)
        self.y = 600
        self.snowflake_size = sd.random_number(15, 40)
        self.gravity = self.snowflake_size / 3

    def move(self):
        wind = sd.random_number(0, 10) - 5
        self.y -= self.gravity
        self.x += wind

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.snowflake_size, color=sd.COLOR_WHITE)

    def can_fall(self):
        return self.y > 10

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.snowflake_size, color=sd.background_color)


def get_flakes(count):
    snowfall = []
    for _ in range(count):
        new_snowflake = Snowflake()
        snowfall.append(new_snowflake)
    return snowfall


def get_fallen_flakes():
    fallen_snowflakes = []

    for number_of_fallen_snowflakes, flake in enumerate(flakes):
        if flake.y < 10:
            fallen_snowflakes.append(number_of_fallen_snowflakes)
    for delta, index in enumerate(fallen_snowflakes):
        flakes.pop(index - delta)
    return len(fallen_snowflakes)


def append_flakes(count):
    for _ in range(count):
        new_snowflake = Snowflake()
        flakes.append(new_snowflake)


flake = Snowflake()

while True:

    flake.clear_previous_picture()
    flake.move()
    flake.draw()

    # TODO есть вопрос: подскажите, пожалуйста, почему используется not, в чем его преимущества?
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

flakes = get_flakes(20)

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()
