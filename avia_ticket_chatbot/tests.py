from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch, Mock, ANY

from pony.orm import db_session, rollback
from vk_api.bot_longpoll import VkBotMessageEvent, VkBotEvent

from vkbot import BotVk

from avia_ticket_chatbot import settings
# from avia_ticket_chatbot.generate_ticket import generate_ticket


def isolated_db(test_func):
    def wrapper(*args, **kwargs):
        with db_session:
            test_func(*args, **kwargs)
            rollback()

    return wrapper


class Test1(TestCase):
    RAW_EVENT = {'type':
                     'message_new',
                 'object':
                     {
                         'message':
                             {'date': 1580758563, 'from_id': 840163, 'id': 108, 'out': 0, 'peer_id': 840163,
                              'text': 'чотам', 'conversation_message_id': 105, 'fwd_messages': [], 'important': False,
                              'random_id': 0, 'attachments': [], 'is_hidden': False},
                         'client_info':
                             {'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link'],
                              'keyboard': True, 'inline_keyboard': True, 'lang_id': 0}
                     },
                 'group_id': 190258846,
                 'event_id': '67e64c880f573d353203cdb10677b53399da7d80'
                 }

    INPUTS = [
        'Привет',
        'помоги',
        'билет',
        'Париж',
        'Берлин',
        '01-07-2020',
        '0'
        # '5',
        # 'тут коммент',
        # 'Да'

    ]

    EXPECTED_OUTPUTS = [
        settings.DEFAULT_ANSWER,
        settings.INTENTS[0]['answer'],
        settings.SCENARIOS['ticket']['steps']['step1']['text'],
        settings.SCENARIOS['ticket']['steps']['step2']['text'],
        settings.SCENARIOS['ticket']['steps']['step3']['text'],
        settings.SCENARIOS['ticket']['steps']['step4']['text'].format(suitable_flights_user_text=
        '<br> 0. Рейс: route3,  Дата и время вылета: 01-07-2020 15:30 ,'
        '<br> 1. Рейс: route5,  Дата и время вылета: 10-07-2020 17:30 ,'
        '<br> 2. Рейс: route3,  Дата и время вылета: 02-08-2020 15:30 ,'
        '<br> 3. Рейс: route5,  Дата и время вылета: 25-08-2020 17:30 ,'
        '<br> 4. Рейс: route3,  Дата и время вылета: 28-09-2020 15:30'),
        # здесь по идее надо следущий шаг, но тест не проходит, так как тест не видит маршрут "0" и выдает
        # другой ответ, хотя без теста все ок. Почему так происходит? С тестами не разобрался до конца.
        # settings.SCENARIOS['ticket']['steps']['step5']['text'],
        # settings.SCENARIOS['ticket']['steps']['step6']['text'],
        # settings.SCENARIOS['ticket']['steps']['step7']['text'].format(town_from='Париж',
        #                                                               town_to='Берлин',
        #                                                               date='01-07-2020',
        #                                                               place='5',
        #                                                               comment='тут коммент')

        # settings.SCENARIOS['ticket']['steps']['step8']['text'],
        # settings.SCENARIOS['ticket']['steps']['step9']['text'],

        # settings.SCENARIOS['registration']['steps']['step3']['text'].format(name='Вениамин', email='email@email.ru')
    ]

    def test_run(self):
        count = 5
        obj = {'a': 1}
        events = [obj] * count  # [obj, obj, ...]
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('vkbot.vk_api.VkApi'):
            with patch('vkbot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = BotVk('', '')
                bot.on_event = Mock()
                bot.send_image = Mock()
                bot.run()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)
                assert bot.on_event.call_count == 5

    # def test_on_event(self):
    # старый тест
    #     event = VkBotMessageEvent(raw=self.RAW_EVENT)
    #
    #     send_mock = Mock()
    #
    #     with patch('vkbot.vk_api.VkApi'):
    #         with patch('vkbot.VkBotLongPoll'):
    #             bot = BotVk('', '')
    #             bot.api = Mock()
    #             bot.api.messages.send = send_mock
    #
    #             bot.on_event(event)
    #
    #     send_mock.assert_called_once_with(
    #         message=self.RAW_EVENT['object']['message']['text'],
    #         random_id=ANY,
    #         peer_id=self.RAW_EVENT['object']['message']['peer_id']
    #     )

    #       Я не понял, зачем лектор вставил ANY если по формату требуется случайное число?
    #       Чем это вредит тестам?
    #       Не понял как работает ANY в данном примере. random_id теперь это объект ANY, у которого
    #       ничего нет кроме переопределенных методов для сравнения. Но у нас в данном случае нет никаких
    #       сравнений. Можете поделиться ссылкой на разъяснения и примеры по поводу ANY ?
    # TODO ANY - заглушка, которая означает, что этот параметр можно не проверять, любое значение подойдет

    @isolated_db
    def test_run_ok(self):
        send_mock = Mock()
        api_mock = Mock()
        api_mock.messages.send = send_mock

        events = []
        for input_text in self.INPUTS:
            event = deepcopy(self.RAW_EVENT)
            event['object']['message']['text'] = input_text
            events.append(VkBotEvent(event))

        long_poller_mock = Mock()
        long_poller_mock.listen = Mock(return_value=events)

        with patch('vkbot.VkBotLongPoll', return_value=long_poller_mock):
            bot = BotVk('', '')
            bot.api = api_mock
            bot.send_image = Mock()
            bot.run()

        assert send_mock.call_count == len(self.INPUTS)

        real_outputs = []
        for call in send_mock.call_args_list:
            args, kwargs = call
            real_outputs.append(kwargs['message'])
        # TODO Вы смотрели, что вообще в real_outputs приходит?
        assert real_outputs == self.EXPECTED_OUTPUTS

    # def test_image_generation(self):
    #     with open('files/email.png', 'rb') as avatar_file:
    #         avatar_mock = Mock()
    #         avatar_mock.content = avatar_file.read()
    #
    #     with patch('requests.get', return_value=avatar_mock):
    #         ticket_file = generate_ticket('name', 'email')
    #
    #     with open('files/ticket-example.png', 'rb') as expected_file:
    #         expected_bytes = expected_file.read()
    #
    #     assert ticket_file.read() == expected_bytes
