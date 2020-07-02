"""
Handler - функция, которая принимает на вход text (текст входящего сообщения) и context (dict), а возвращает bool:
True, если шаг пройден, False, если данные введены неправильно.

"""
import datetime
import random
import re

from avia_ticket_chatbot.generate_ticket import generate_ticket
from avia_ticket_chatbot.models import UserState
from avia_ticket_chatbot.settings import DISPATCHER_CONFIG

# re_name = re.compile(r'^[\w\-\s]{3,40}$')
# re_email = re.compile(r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b")

re_towns = {
    r'[Мм]оскв\w{0,}': 'Москва',
    r'[Сс]анкт-Петербург\w{0,}': 'Санкт-Петербург',
    r'[Вв]ладивосток\w{0,}': 'Владивосток',
    r'[Пп]ариж\w{0,}': 'Париж',
    r'[Бб]ерли\w{0,}': 'Берлин',

}

re_date = re.compile(r'\d\d-\d\d-\d{4}')
re_place = [1, 2, 3, 4, 5]
re_phone = re.compile(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")


def handle_town_from(text, context, id):
    for re_town in re_towns:
        re_town_comp = re.compile(re_town)
        match = re.match(re_town_comp, text)
        if match:
            for route in DISPATCHER_CONFIG:
                if re_towns[re_town] == DISPATCHER_CONFIG[route]['town_from']:
                    context['town_from'] = re_towns[re_town]
                    return True

    town_dict = set()
    for route in DISPATCHER_CONFIG:
        town_dict.add(DISPATCHER_CONFIG[route]['town_from'])
    context['town_from'] = ', '.join(town_dict)
    return False


def handle_town_to(text, context, id):
    for re_town in re_towns:
        re_town_comp = re.compile(re_town)
        match = re.match(re_town_comp, text)
        if match:
            for route in DISPATCHER_CONFIG:
                if re_towns[re_town] == DISPATCHER_CONFIG[route]['town_to']\
                        and context['town_from'] == DISPATCHER_CONFIG[route]['town_from']:
                    context['town_to'] = re_towns[re_town]
                    return True
            else:
                context['town_to'] = re_towns[re_town]
                state = UserState.get(user_id=id)
                state.step_name = 'no_flights_between'
                return True
    town_dict = set()
    for route in DISPATCHER_CONFIG:
        town_dict.add(DISPATCHER_CONFIG[route]['town_to'])
    context['town_to'] = ', '.join(town_dict)
    return False


def handle_date_format(text, context, id):
    now = datetime.datetime.now()
    match = re.match(re_date, text)
    if match:
        print(text, match, '+++')  # TODO Тут дату распознает верно
        incoming_date_datetime = datetime.datetime.strptime(text, '%d-%m-%Y')
        delta = datetime.timedelta(hours=now.hour + 1, minutes=now.minute, seconds=now.second)
        incoming_date_datetime += delta
        if incoming_date_datetime >= datetime.datetime.now():  # TODO А вот здесь проблема
            # TODO Дата в тестах не будет больше или равна текущей дате
            # TODO Исправление этой ошибки зависит от формирования словаря с датами
            # TODO в идеале в тесте надо использовать дату запуска теста (вместо 01-07-2020)
            # TODO и под неё формировать ответ
            context['date'] = text
            print(text, match, '+++')
            return True
    return False


def handle_flight_selection(text, context, id):
    if text in context['suitable_flights']:
        context['route'] = context['suitable_flights'][text]
        return True
    return False


def handle_number_of_seats(text, context, id):
    if text.isdigit():
        if int(text) in re_place:
            context['place'] = text
        return True
    return False


def handle_comment(text, context, id):
    context['comment'] = text
    return True


def handle_yesno(text, context, id):
    if text == 'Да':
        return True
    elif text == 'Нет':
        state = UserState.get(user_id=id)
        state.step_name = 'user_mistake'
        return True
    return False


def handle_phone_number(text, context, id):
    match = re.match(re_phone, text)
    if match:
        context['phone'] = text
        return True
    else:
        return False


def generate_ticket_handler(text, context):
    return generate_ticket(name=context['name'], email=context['email'])
