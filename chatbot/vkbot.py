# -*- coding: utf-8 -*-
from datetime import time
from pprint import pprint
import random
import logging

from chatbot import handlers

try:
    import settings
except ImportError:
    exit('Скопируй из settings.py.default в settings.py и установи TOKEN!')

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

log = logging.getLogger('bot')


def configure_logging():
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('bot.log')

    stream_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))

    file_handler.setFormatter(logging.Formatter(fmt='%(asctime)s %(levelname)s %(message)s', datefmt='%d-%m-%Y %H:%M'))

    log.addHandler(stream_handler)
    log.addHandler(file_handler)

    stream_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)
    log.setLevel(logging.DEBUG)


class UserState:
    """
    Состояние пользователя внутри сценария.
    """

    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {}

    # TODO: def __init__(self, scenario_name, step_name, context={}):
    #  не понял объяснение лектора - почему так делать нельзя, почему при добавлении новой ID
    #  все равно будет ссылаться на один и тот же дикт контекста? И чем лучше строка self.context = context or {}
    #  Разве это не одно и тоже? Разъясните, пожалуйста.


class BotVk:
    """
    Сценарий регистрации на конференцию через vk.com

    Поддерживает ответы на вопросы про дату, место проведения и сценарий регистрации:
    - спрашиваем имя
    - спрашиваем e-mail
    - говорим об успешной регистрации
    Если шаг не пройден, задаем уточняющий вопрос пока шаг не будет пройден.
    use Python 3.7
    Echo bot for VK.com

    """

    def __init__(self, id_group, token):

        """

        :param id_group:  gpoup_id из группы vk
        :param token: секретный token
        """
        self.id_group = id_group
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(self.vk, self.id_group)
        self.api = self.vk.get_api()
        self.user_states = dict()  # user_id -> UserState

    def run(self):
        """
        запуск бота

        """
        for event in self.long_poller.listen():

            try:
                self.on_event(event)
            except Exception:
                log.exception('Ошибка в обработке события.')

    def on_event(self, event):
        """
         Обрабатывает сообщения бота. Отправляет сообщение назад, если это текст

        :param event: VKBotMessageEvent object
        :return:
        """
        if event.type != VkBotEventType.MESSAGE_NEW:
            log.info('Мы пока не умеем обрабатывать события такого типа. {}'.format(event.type))
            return

        user_id = event.message.peer_id
        text = event.message.text

        if user_id in self.user_states:
            # продолжаем сценарий

            text_to_send = self.continue_scenario(user_id, text=text)


        else:
            # ищем intent
            for intent in settings.INTENTS:
                if any(token in text.lower() for token in intent['tokens']):
                    # run intent
                    if intent['answer']:
                        text_to_send = intent['answer']
                    else:
                        text_to_send = self.start_scenario(user_id, intent['scenario'])
                    break
            else:
                text_to_send = settings.DEFAULT_ANSWER

        self.api.messages.send(message=text_to_send,
                               random_id=random.randint(0, 2 ** 20),
                               peer_id=user_id
                               )

    def continue_scenario(self, user_id, text):
        state = self.user_states[user_id]
        steps = settings.SCENARIOS[state.scenario_name]['steps']
        step = steps[state.step_name]
        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context):
            # next step
            next_step = steps[step['next_step']]
            text_to_send = next_step['text'].format(**state.context)
            if next_step['next_step']:
                # switch to next step
                state.step_name = step['next_step']
            else:
                # finish scenario
                self.user_states.pop(user_id)
        else:
            # retry current step
            text_to_send = step['failure_text'].format(**state.context)

        return text_to_send

    def start_scenario(self, user_id, scenario_name):
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        self.user_states[user_id] = UserState(scenario_name=scenario_name, step_name=first_step)
        return text_to_send


if __name__ == "__main__":
    configure_logging()
    BotDrink = BotVk(settings.ID_GROUP, settings.TOKEN)
    BotDrink.run()

    # а как лектор понял, что можно так написать? Почему мы не создавали объект класса VkBotEventType?
    #  Что-то похожее мы делали с элементами в 7.02
    #  Про объект вопроса не понял, мы получаем на вход объект и пытаемся узнать его класс
    #  Это один из способов
    #  я думал, что прежде чем обращаться к методам и атрибутам класса необходимо создать его
    # экземпляр, вот это выражение vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW сразу обращается
    # к классу который мы не создавали, либо я этот момент упустил.
    #  Класс создаётся вот этим методом из bot_longpoll
    """
    def _parse_event(self, raw_event):
        event_class = self.CLASS_BY_EVENT_TYPE.get(
            raw_event['type'],
            self.DEFAULT_EVENT_CLASS
        )
        return event_class(raw_event)
    """
    # Поясните пожалуйста что делают эти строчки кода?
    #  В одном из первых модулей мы создавали словарь с функциями, которые потом можно было вытащить
    #  по ключу и использовать (задание 4.03).
    #  Это примерно такая же структура, только с Классами, вернее с Классом
    #  Так, по ключу мы сможем создать объект нужного класса
    #  Вот там далее это используется
    #  хорошо давайте вернемся к уроку 4:
    #  {'name': 'Треугольник', 'func': triangle}
    #  func_of_dict = figures[user_figure]['func']
    #  func_of_dict(point=point, length=length, angle=0, color_figure=figures_color)
    #  triangle - какой это объект в первой строчке? это и не текст и не вызов функции, ссылка?
    #  Это вполне можно проверить при помощи type(triangle), в данном случае это функция
    #  Функция, как и Класс могут быть объектами (когда указаны без скобок)
    #  В таком виде их можно хранить, например, в словаре
    #  Далее мы берем объект из словаря figures[user_figure]['func']
    #  Читаем название словаря -- Идём в этот словарь -- По ключам приходим к функции
    #  В итоге привязываем к переменной ссылку на объект-функцию
    #  И далее с этой переменной можно обращаться как с функцией - добавить () для вызова тела функции
    #  func_of_dict(point=point, length=length, angle=0, color_figure=figures_color)
    #  срабатывает тело функции
    #  вторая строчка как я понимаю, func_of_dict тоже ссылка на определение функции, наверное
    #  такие приемы просто зашиты в интерпретатор и мне надо запомнить? Так как логики я не вижу)
    #  Я понимаю определение функции и вызов функции, а такой подход не понимаю, помогите пожалуйста)
    # def _parse_event(self, raw_event):
    #     event_class = self.CLASS_BY_EVENT_TYPE.get(
    #         raw_event['type'],
    #         self.DEFAULT_EVENT_CLASS
    #     )  #  Тут получают класс из словаря
    #     return event_class(raw_event)
    #  Здесь мы получаем объект-класс из словаря self.CLASS_BY_EVENT_TYPE
    #  Привязываем его к переменной event_class и далее создаем объект привязанного класса
    #  event_class(параметр) -- создание объекта
    #  пайтон идёт по ссылки и читает это как VkBotMessageEvent(параметр)
    #   Тут возвращают объект этого класса (добавлены скобки для создания объекта)

    # Классы для событий по типам
    #     CLASS_BY_EVENT_TYPE = {
    #         VkBotEventType.MESSAGE_NEW.value: VkBotMessageEvent,
    #         VkBotEventType.MESSAGE_REPLY.value: VkBotMessageEvent,
    #         VkBotEventType.MESSAGE_EDIT.value: VkBotMessageEvent,
    #     }
    #
    #     #: Класс для событий
    #     DEFAULT_EVENT_CLASS = VkBotEvent
    # Это нормально, что у меня столько вопросов на 4 месяце обучения?
    #  Это нормально. Хорошо, что вы изучаете библиотеки изнутри
    #  Однако обратите внимание, что все вопросы (кроме наверное DotDict) касаются кода
    #  В котором используются знакомые вам приемы, просто немного измененные/необычные
    #  Это наверное первая библиотека на курсе, которую необходимо изнутри изучить
    #  Она не простая, но важно помнить, что она состоит из простых частей
    #  Старайтесь находить все зависимости, переменные, чьи имена используются, думайте о типах
    #  используемых объектов
    # Хочется подробно обсудить эту библиотеку, последовательно, что - откуда, и почему.
    # Мне кажется будет очень полезно для студентов добавить урок в раздел интроспекции, где
    #  подробно разберут какую - нибудь библиотеку, построчно, досконально. Я не просто так сросил,
    #  нормально ли такое количество вопросов у меня, так как после этого раздела у меня сложилось ощущение,
    #  что я не совсем поспеваю за лектором, как-будто пропустил пару десятков лекций. Что называется
    #  "с места в карьер". Как мне быть?
    #  Предложение такое можете направить на hello@skillbox.ru
    #  Но не уверен, насколько будет это эффективно.
    #  На данном этапе от вас не требует досконального понимания библиотеки (без серьезных затрат по времени
    #  я сам не скажу, что досканально разбираюсь в ней, она довольно обширна)
    #  Могу посоветовать читать больше документации и сидеть часами, выслеживая взаимодействия объектов
    #  до самых простых сущностей (все сложные объекты рано или поздно распадаются на мелкие
    #  А мелкие либо вам известны, либо можно почитать о них в документации)
    #  Скорость осваивания таких библиотек растёт со временем.
    #  Работа с документацией - это уже опыт, который вам надо набирать самостоятельно

# Вопрос - подскажите, пож, почему недостаточно просто импорта vk_api - в видеоуроке это не объясняется,
# кусок вырезан, import vk_api.bot_longpoll просто появляется в какой-то момент.
#  vk_api это по сути пакет, если пройдете по ссылке - попадете в __init__
#  И в нём прописаны автоматические импорты (минимум для работы с библиотекой)
#  Среди этого минимума нету нужного нам bot_longpoll
#  (возможно его исключили из автоматического импорта после урока)

# C этой конструкцией не разобрался, что она делает?
# class DotDict(dict):
#     __getattr__ = dict.get
#     __setattr__ = dict.__setitem__
#     __delattr__ = dict.__delitem__
#  Эта конструкция позволяет получать доступ к элементам словаря через точку
#  словарь = {'val': '123'}
#  словарь = DotDict(словарь)
#  словарь.val --> Это будет равно значению '123'
# для чего конструкция я понял, непонятно как это работает на уровне интерпретатора
# а можно чуть подробнее - класс DotDict наследуется от словаря, что происходит потом?
# __getattr__ по идее метод, его не переопределяют а присваивают ему я так думаю метод словаря,
#  мы так не делали, поэтому такая конструкция у меня вызывает недоумение, я не понимаю как это работает.
#  Что-то похожее мы обсуждали с вами только что) про переопределение requests.get
#  Мы заменяем методы словаря, __getattr__ позволяет нам получать атрибут, по его имени через точку
#  Заменив его мы при попытке получить атрибут запускаем метод get, где ключом будет имя, записанное через точку
#  Подробнее можно узнать почитав в документации словаря о методах, с которыми он работает
# B и еще вопрос, не всегда через "." в списке появляются нужные атрибуты/классы с чем это может быть связано?
# Не понял вопрос, возможно он связан с тем, на что я ответил выше
# когда я набираю текст кода, иногда для удобства я через точку пытаюсь достучать до каких-то атрибутов
#  или методов, с этой библиотекой у меня многое не отображалось приходилось копировать, почему так происходит?
#  А, это фича пайчарма, которая работает, когда может найти очевидные ссылки на объект
#  Если структура усложняется, то приходится всё искать вручную
