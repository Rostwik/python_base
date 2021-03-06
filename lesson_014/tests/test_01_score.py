# -*- coding: utf-8 -*-


import unittest
from unittest.mock import Mock

from lesson_014.bowling import get_score

_test_data1 = ''
_test_data2 = '2/37X19111111--2821'
_test_data6 = 'XXXXXXXXXX'
_test_data3 = '2/--X-1XX-/------'
_test_data4 = '-/-/-/-/-/-/-/-/-/----'
_test_data5 = '2/37X19111111--282'



# не могу понять почему запускается только один тест, а не два. Подскажите, пож.
#  Проверка правильных вариантов разных видов - это хорошо, но это только один из вариантов работы программы
#  Старайтесь исходить из 3 основных типов ввода:
#  ничего (пустая строка)
#  много всего(очень длинная строка правильных/неправильных символов)
#  ввод нужного размера (правильный/неправильный)
class GetScoreTest(unittest.TestCase):

    def test_normal(self):
        fake_result = Mock()
        fake_result.text = _test_data1
        get_score(fake_result.text)

    def test_normal_2(self):
        fake_result = Mock()
        fake_result.text = _test_data2
        result = get_score(fake_result.text)
        self.assertEqual(result, 74)

    def test_normal_3(self):
        fake_result = Mock()
        fake_result.text = _test_data5
        #get_score(fake_result.text)
        with self.assertRaises(Exception) as err:
            get_score(fake_result.text)
        self.assertEqual('Проверьте данные - неверное количество символов!', str(err.exception))

    def test_normal_4(self):
        fake_result = Mock()
        fake_result.text = _test_data6
        get_score(fake_result.text)
        result = get_score(fake_result.text)
        self.assertEqual(result, 200)

    def test_hard(self):
        fake_result = Mock()
        fake_result.text = _test_data3
        result = get_score(fake_result.text)
        self.assertEqual(result, 91)

    def test_hard2(self):
        fake_result = Mock()
        fake_result.text = _test_data4
        result = get_score(fake_result.text)
        self.assertEqual(result, 135)


if __name__ == '__main__':
    unittest.main()
