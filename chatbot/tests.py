from unittest import TestCase
from unittest.mock import patch, Mock, ANY

from vk_api.bot_longpoll import VkBotMessageEvent

from vkbot import BotVk


class Test1(TestCase):

    RAW_EVENT = {'type':
                     'message_new',
                 'object':
                    {
                     'message':
                         {'date': 1580758563, 'from_id': 840163, 'id': 108, 'out': 0, 'peer_id': 840163, 'text': 'чотам', 'conversation_message_id': 105, 'fwd_messages': [], 'important': False, 'random_id': 0, 'attachments': [], 'is_hidden': False},
                     'client_info':
                         {'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link'],
                          'keyboard': True, 'inline_keyboard': True, 'lang_id': 0}
                    },
                 'group_id': 190258846,
                 'event_id': '67e64c880f573d353203cdb10677b53399da7d80'
                 }

    def test_run(self):
        count = 5
        obj = {'a': 1}
        events = [obj] * count # [obj, obj, ...]
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('vkbot.vk_api.VkApi'):
            with patch('vkbot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = BotVk('', '')
                bot.on_event = Mock()
                bot.run()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)
                assert bot.on_event.call_count == 5

    def test_on_event(self):
        event = VkBotMessageEvent(raw=self.RAW_EVENT)

        send_mock = Mock()

        with patch('vkbot.vk_api.VkApi'):
            with patch('vkbot.VkBotLongPoll'):
                bot = BotVk('', '')
                bot.api = Mock()
                bot.api.messages.send = send_mock

                bot.on_event(event)

        send_mock.assert_called_once_with(
            message=self.RAW_EVENT['object']['message']['text'],
            random_id=ANY,
            peer_id=self.RAW_EVENT['object']['message']['peer_id']
        )

        #       Я не понял, зачем лектор вставил ANY если по формату требуется случайное число?
        #       Чем это вредит тестам?
        #       Не понял как работает ANY в данном примере. random_id теперь это объект ANY, у которого
        #       ничего нет кроме переопределенных методов для сравнения. Но у нас в данном случае нет никаких
        #       сравнений. Можете поделиться ссылкой на разъяснения и примеры по поводу ANY ?

