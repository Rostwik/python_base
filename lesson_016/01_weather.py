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

import pytz
import datetime
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import cv2


class WeatherMaker:

    def __init__(self, url, number_of_days):
        self.url = url
        self.number_of_days = number_of_days

    def weather_html(self):
        result = {}

        response = requests.get(self.url)
        if response.status_code == 200:
            html_doc = BeautifulSoup(response.text, features='html.parser')
            list_of_nods = html_doc.find_all('div', {'class': 'forecast-briefly__day'})
            today = datetime.datetime.now(pytz.timezone('Europe/Moscow'))

            for tag in list_of_nods:

                data_dt = datetime.datetime.strptime(tag.time['datetime'], '%Y-%m-%d %H:%M%z')
                data_str = tag.time['datetime']
                if -1 <= (data_dt - today).days <= self.number_of_days:
                    result[data_str] = [tag.find_all('span', {'class': 'temp__value'})[0].text]
                    result[data_str].append(tag.find_all('div', {'class': 'forecast-briefly__condition'})[0].text)
                    return result
        # pprint(result)


class ImageMaker:
    def __init__(self):
        pass

    def draw_a_card(self, condition, temperature):
        path = 'python_snippets/external_data/weather_img/'
        cloud = ['Пасмурно', 'Облачно', 'Облачно с прояснениями']
        if condition in cloud:
            img = 'cloud.jpg'
        image = cv2.imread(path + img)

        cv2.putText(image, condition, (15, 50),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5,
                    (255, 0, 0), 2)
        cv2.putText(image, temperature, (40, 65),
                    cv2.FONT_HERSHEY_COMPLEX, 0.4,
                    (255, 0, 0), 2)

        cv2.imshow('Original', image)
        cv2.imwrite("flip.png", image)
        cv2.waitKey(0)


perfect_day = WeatherMaker('https://yandex.ru/pogoda/saint-petersburg', 3)
weather_data = perfect_day.weather_html()

postcard = ImageMaker()
postcard.draw_a_card('Облачно', '+2')
