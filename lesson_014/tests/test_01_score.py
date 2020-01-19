# -*- coding: utf-8 -*-


import unittest
from unittest.mock import Mock

from lesson_014.bowling import get_score

_test_data1 = '2/37X11111111--2821'
_test_data2 = '2/37X19111111--2821'

# TODO: не могу понять почему запускается только один тест, а не два. Подскажите, пож.

class GetScoreTest(unittest.TestCase):

    def test_normal(self):
        fake_result = Mock()
        fake_result.text = _test_data1
        result = get_score(fake_result.text)
        self.assertEqual(result, 66)

    def test_normal_2(self):
        fake_result = Mock()
        fake_result.text = _test_data2
        result = get_score(fake_result.text)
        self.assertEqual(result, 74)


if __name__ == '__main__':
    unittest.main()
