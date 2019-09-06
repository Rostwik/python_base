#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}
distances['Moscow'] = {}
distances['Moscow']['London'] = ((sites['Moscow'][0]-sites['London'][0]) ** 2 + (sites['Moscow'][1]-sites['London'][1]) ** 2) ** 0.5
distances['Moscow']['Paris'] = ((sites['Moscow'][0]-sites['Paris'][0]) ** 2 + (sites['Moscow'][1]-sites['Paris'][1]) ** 2) ** 0.5




print(distances)




