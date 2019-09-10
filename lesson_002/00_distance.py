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


sites_moscow = sites['Moscow']
sites_london = sites['London']
sites_paris = sites['Paris']

distances['Moscow'] = {}

moscow_london = (((sites_moscow[0] - sites_london[0]) ** 2
                  + (sites_moscow[1] - sites_london[1]) ** 2) ** 0.5)
moscow_paris = (((sites_moscow[0] - sites_paris[0]) ** 2
                 + (sites_moscow[1] - sites_paris[1]) ** 2) ** 0.5)

distances['London'] = {}

london_moscow = moscow_london
london_paris = ((sites_london[0] - sites_paris[0]) ** 2 + (
            sites_london[1] - sites_paris[1]) ** 2) ** 0.5

distances['Paris'] = {}

paris_moscow = moscow_paris
paris_london = london_paris

distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris
distances['London']['Moscow'] = london_moscow
distances['London']['Paris'] = london_paris
distances['Paris']['Moscow'] = paris_moscow
distances['Paris']['London'] = paris_london

print(distances)