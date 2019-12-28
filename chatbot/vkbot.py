# -*- coding: utf-8 -*-
from pprint import pprint
import random

from chatbot._token import token
import vk_api
import vk_api.bot_longpoll

# TODO: Вопрос - подскажите, пож, почему недостаточно просто импорта vk_api - в видеоуроке это не объясняется,
# TODO: кусок вырезан, import vk_api.bot_longpoll просто появляется в какой-то момент.

# TODO: C этой конструкцией не разобрался, что она делает?
# TODO:  class DotDict(dict):
#     __getattr__ = dict.get
#     __setattr__ = dict.__setitem__
#     __delattr__ = dict.__delitem__
# TODO: B и еще вопрос, не всегда через "." в списке появляются нужные атрибуты/классы с чем это может быть связано?


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

            # TODO: а как лектор понял, что можно так написать? Почему мы не создавали объект класса VkBotEventType?
            # TODO: Поясните пожалуйста что делают эти строчки кода?
            # TODO Классы для событий по типам
            #     CLASS_BY_EVENT_TYPE = {
            #         VkBotEventType.MESSAGE_NEW.value: VkBotMessageEvent,
            #         VkBotEventType.MESSAGE_REPLY.value: VkBotMessageEvent,
            #         VkBotEventType.MESSAGE_EDIT.value: VkBotMessageEvent,
            #     }
            # TODO
            #     #: Класс для событий
            #     DEFAULT_EVENT_CLASS = VkBotEvent
            # TODO: Это нормально, что у меня столько вопросов на 4 месяце обучения?
            # TODO: Хочется подробно обсудить эту библиотеку, последовательно, что - откуда, и почему.

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
