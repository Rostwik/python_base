#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка

import simple_draw as sd

snowfall = []
fallen_snowflakes = []


def create_a_snowflake(n):
    for _ in range(n):
        x = sd.random_number(50, 1150)
        y = 600
        n = sd.random_number(15, 40)
        snowfall.append([x, y, n])


def move_snowflake():
    for icecrystal in snowfall:
        gravity = icecrystal[2] / 3
        wind = sd.random_number(0, 10) - 5
        icecrystal[1] -= gravity
        icecrystal[0] += wind


def draw_color_snowflakes(color):
    for icecrystal in snowfall:
        point = sd.get_point(icecrystal[0], icecrystal[1])
        sd.snowflake(center=point, length=icecrystal[2], color=color)


def down_snowflakes():
    for number_of_fallen_snowflakes, icecrystal in enumerate(snowfall):
        if icecrystal[1] < 10:
            fallen_snowflakes.append(number_of_fallen_snowflakes)

    return fallen_snowflakes


def delete_snowflakes(*args):
    global fallen_snowflakes
    fallen_snowflakes = []

    for delta, index in enumerate(args):
        snowfall.pop(index - delta)
#зачет!