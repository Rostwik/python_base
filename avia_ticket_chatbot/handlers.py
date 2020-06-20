"""
Handler - функция, которая принимает на вход text (текст входящего сообщения) и context (dict), а возвращает bool:
True, если шаг пройден, False, если данные введены неправильно.

"""
import re

from avia_ticket_chatbot.generate_ticket import generate_ticket
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


def handle_town_from(text, context):
    for re_town in re_towns:
        re_town_comp = re.compile(re_town)
        match = re.match(re_town_comp, text)
        if match:
            for route in DISPATCHER_CONFIG:
                if re_towns[re_town] == DISPATCHER_CONFIG[route]['town_from']:
                    context['town_from'] = re_towns[re_town]
                    return True

    town_dict = []
    for route in DISPATCHER_CONFIG:
        town_dict.append(DISPATCHER_CONFIG[route]['town_from'])
    context['town_from'] = ', '.join(town_dict)
    return False


def handle_town_to(text, context):
    for re_town in re_towns:
        re_town_comp = re.compile(re_town)
        match = re.match(re_town_comp, text)
        if match:
            for route in DISPATCHER_CONFIG:
                if re_towns[re_town] == DISPATCHER_CONFIG[route]['town_to']:
                    context['town_to'] = re_towns[re_town]
                    return True

    town_dict = []
    for route in DISPATCHER_CONFIG:
        town_dict.append(DISPATCHER_CONFIG[route]['town_to'])
    context['town_to'] = ', '.join(town_dict)
    return False


def handle_date_format(text, context):
    match = re.match(re_date, text)
    if match:
        context['date'] = text
        return True
    return False


def handle_flight_selection(text, context):
    if text in context['suitable_flights']:
        context['route'] = text
        return True
    return False


def handle_number_of_seats(text, context):
    if text.isdigit():
        if int(text) in re_place:
            context['place'] = text
        return True
    return False


def handle_comment(text, context):
    context['comment'] = text
    return True


def handle_yesno(text, context):
    # TODO дописать функцию handle_yesno

    return True


def handle_phone_number(text, context):
    match = re.match(re_phone, text)
    if match:
        context['phone'] = text
        return True
    else:
        return False


def generate_ticket_handler(text, context):
    return generate_ticket(name=context['name'], email=context['email'])
