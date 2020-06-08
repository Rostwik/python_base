"""
Handler - функция, которая принимает на вход text (текст входящего сообщения) и context (dict), а возвращает bool:
True, если шаг пройден, False, если данные введены неправильно.

"""
import re

from avia_ticket_chatbot.generate_ticket import generate_ticket
from avia_ticket_chatbot.settings import DISPATCHER_CONFIG

re_name = re.compile(r'^[\w\-\s]{3,40}$')
re_email = re.compile(r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b")

def handle_town_from(text, context):
    for route in DISPATCHER_CONFIG:
        re_town =
        if route['town_from'] == text:
            context['town_from'] = text
        elif

        else:

    match = re.match(re_name, text)
    if match:
        context['town_from'] = text
        return True
    else:
        print('Возможно Вы имели в виду')
        return False

def handle_town_to(text, context):
    return True

def handle_name(text, context):
    match = re.match(re_name, text)
    if match:
        context['name'] = text
        return True
    else:
        return False


def handle_email(text, context):
    matches = re.findall(re_email, text)
    if len(matches) > 0:
        context['email'] = matches[0]
        return True
    else:
        return False


def generate_ticket_handler(text, context):
    return generate_ticket(name=context['name'], email=context['email'])
