# -*- coding: utf-8 -*-
from pprint import pprint
import random

from chatbot._token import token
import vk_api
import vk_api.bot_longpoll

# Вопрос - подскажите, пож, почему недостаточно просто импорта vk_api - в видеоуроке это не объясняется,
# кусок вырезан, import vk_api.bot_longpoll просто появляется в какой-то момент.
# TODO vk_api это по сути пакет, если пройдете по ссылке - попадете в __init__
# TODO И в нём прописаны автоматические импорты (минимум для работы с библиотекой)
# TODO Среди этого минимума нету нужного нам bot_longpoll
# TODO (возможно его исключили из автоматического импорта после урока)

# C этой конструкцией не разобрался, что она делает?
# class DotDict(dict):
#     __getattr__ = dict.get
#     __setattr__ = dict.__setitem__
#     __delattr__ = dict.__delitem__
# TODO Эта конструкция позволяет получать доступ к элементам словаря через точку
# TODO словарь = {'val': '123'}
# TODO словарь = DotDict(словарь)
# TODO словарь.val --> Это будет равно значению '123'

# B и еще вопрос, не всегда через "." в списке появляются нужные атрибуты/классы с чем это может быть связано?
# TODO Не понял вопрос, возможно он связан с тем, на что я ответил выше

id_group = 190258846


class BotVk:

    def __init__(self, id_group, token):
        self.id_group = id_group
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(self.vk, self.id_group)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            print('получено событие')
            try:
                self.on_event(event)
            except Exception as exp:
                print(exp)

    def on_event(self, event):
        if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:

            # а как лектор понял, что можно так написать? Почему мы не создавали объект класса VkBotEventType?
            # TODO Что-то похожее мы делали с элементами в 7.02
            # TODO Про объект вопроса не понял, мы получаем на вход объект и пытаемся узнать его класс
            # TODO Это один из способов

            # Поясните пожалуйста что делают эти строчки кода?
            # TODO В одном из первых модулей мы создавали словарь с функциями, которые потом можно было вытащить
            # TODO по ключу и использовать (задание 4.03).
            # TODO Это примерно такая же структура, только с Классами, вернее с Классом
            # TODO Так, по ключу мы сможем создать объект нужного класса
            # TODO Вот там далее это используется
            # def _parse_event(self, raw_event):
            #     event_class = self.CLASS_BY_EVENT_TYPE.get(
            #         raw_event['type'],
            #         self.DEFAULT_EVENT_CLASS
            #     )  # TODO Тут получают класс из словаря
            #     return event_class(raw_event)
            #  TODO Тут возвращают объект этого класса (добавлены скобки для создания объекта)

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
            # TODO Это нормально. Хорошо, что вы изучаете библиотеки изнутри
            # TODO Однако обратите внимание, что все вопросы (кроме наверное DotDict) касаются кода
            # TODO В котором используются знакомые вам приемы, просто немного измененные/необычные
            # TODO Это наверное первая библиотека на курсе, которую необходимо изнутри изучить
            # TODO Она не простая, но важно помнить, что она состоит из простых частей
            # TODO Старайтесь находить все зависимости, переменные, чьи имена используются, думайте о типах
            # TODO используемых объектов
            # Хочется подробно обсудить эту библиотеку, последовательно, что - откуда, и почему.

            print(event.message.text)

            self.api.messages.send(message=event.message.text,
                                   random_id=random.randint(0, 2 ** 20),
                                   peer_id=event.message.peer_id
                                   )
        else:
            print("Мы пока не умеем обрабатывать события такого типа.", event.type)


if __name__ == "__main__":
    BotDrink = BotVk(id_group, token)
    BotDrink.run()
