# -*- coding: utf-8 -*-


# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено, и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погоды
# из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database

import datetime
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import cv2
import os

from lesson_016.instruments import pars_date


class WeatherMaker:

    def __init__(self, url):
        self.url = url

    def weather_html(self, start_date=None, end_date=None, init=True):

        result = {}

        if init:
            start_date = datetime.date.today() - datetime.timedelta(days=7)
            end_date = datetime.date.today()
        else:
            start_date = pars_date(start_date)
            end_date = pars_date(end_date)

        response = requests.get(self.url)
        if response.status_code == 200:
            html_doc = BeautifulSoup(response.text, features='html.parser')
            list_of_nods = html_doc.find_all('div', {'class': 'forecast-briefly__day'})

            for tag in list_of_nods:

                date_str, timezone = tag.time['datetime'].split(' ')
                date_dt = pars_date(date_str)

                if start_date <= date_dt <= end_date:
                    result[date_str] = [tag.find_all('span', {'class': 'temp__value'})[0].text]
                    result[date_str].append(tag.find_all('div', {'class': 'forecast-briefly__condition'})[0].text)

            return result


class ImageMaker:

    # Солнечно - от желтого к белому
    # Дождь - от синего к белому
    # Снег - от голубого к белому
    # Облачно - от серого к белому

    def draw_a_card(self, condition, temperature, date):

        path_parent = 'python_snippets/external_data/weather_img/'
        path_bg = 'python_snippets/external_data/weather_gradient/'

        directory = date.replace('-', '')[:6]

        path = os.path.join(path_parent, directory)
        try:
            os.mkdir(path)
        except OSError:
            print('Создание директории не требуется.')

        cloud = ['Пасмурно', 'Облачно', 'Облачно с прояснениями', 'Малооблачно']
        rain = ['Дождь со снегом', 'Небольшой дождь']
        if condition in cloud:
            img = 'cloud.jpg'
            img_bg = 'cloudy.jpg'
        elif condition in rain:
            img = 'rain.jpg'
            img_bg = 'rainy.jpg'
        elif condition == 'снег':
            img = 'snow.jpg'
            img_bg = 'snowy.jpg'
        elif condition == 'Ясно':
            img = 'sun.jpg'
            img_bg = 'sunny.jpg'
        else:
            print('Подходящие погодные условия не найдены, установлен фон по умолчанию.')
            img = 'rain.jpg'
            img_bg = 'rainy.jpg'
        # TODO Я кажется понял, почему у вас получается такая маленькая открытка
        # TODO Для основы нужно использовать lesson_016/python_snippets/external_data/probe.jpg
        # TODO Это белая пустая картинка, на которую можно добавить всю нужную информацию
        image = cv2.imread(path_parent + img)
        background = cv2.imread(path_bg + img_bg)
        postcard = cv2.addWeighted(image, 0.5, background, 0.5, 0)
        few_words_condition = condition.split(' ')
        delta = 0

        for word in few_words_condition:
            cv2.putText(postcard, word, (2, 30 + delta), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
            delta += 15
        cv2.putText(postcard, temperature, (40, 80), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)

        os.chdir(path)  # TODO Эта команда будет выдавать ошибку, если мы уже находимся в нужной папке
        # TODO тут, как мне кажется лучше прописывать путь от директории, в которой запущена программа
        # TODO чтобы не запутаться при множественном создании открыток за одну сессию

        cv2.imwrite(str(date) + 'postcard.png', postcard)
        # TODO После создания удобно было бы видеть путь по которому была создана открытка