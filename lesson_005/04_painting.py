# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd
from lesson_005.painting.humanity.house import house
from lesson_005.painting.nature.tree import draw_branches
from lesson_005.painting.nature.rainbow import unicorn_road
from lesson_005.painting.humanity.smile import smile
from lesson_005.painting.nature.snow import snowdrift
from lesson_005.painting.nature.sun import sun

sd.resolution = (1600, 800)

left_bottom = sd.get_point(0, 0)
right_top = sd.get_point(1600, 100)

sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_ORANGE, width=0)

point_tree = sd.get_point(1300, 100)
draw_branches(point=point_tree, angle=90, length=100)
point_tree = sd.get_point(1100, 100)
draw_branches(point=point_tree, angle=90, length=50)

house(400, 100)
smile(660, 250, color=sd.COLOR_CYAN)
unicorn_road(800)
snowdrift(100, 100, 10)
sun(800, 650)

sd.pause()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
#зачет!