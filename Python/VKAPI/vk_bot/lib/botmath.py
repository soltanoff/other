#!/usr/bin/env python
# -*- coding: utf8 -*-
from math import *

import emoji

from cfg.config import SAVE_LIST


class BotMath(object):
    def __init__(self):
        self._safe_dict = dict([(k, globals().get(k, None)) for k in SAVE_LIST])
        self._safe_dict['abs'] = abs

    @staticmethod
    def get_help():
        return emoji.emojize(u"""
            :bulb: Ключевые литералы и их особенности для математики бота:
             :small_blue_diamond: Сложение, Вычитание, Умножение, Разность: \'+\' \'-\' \'*\' \'/\'
             :small_blue_diamond: Дробные числа используют символ \'.\': 2.5
             :small_blue_diamond: Приоритеты операций определяются по правилам математики. Так же можно использовать круглые скобки
             :warning: Особенности деления:
             \tПроисходит деление либо целых чисел (результат целое), либо вещественных.
             \tНапример: 5/2 = 2, 5/2.0 = 2.5

            :book: Доступные функции:
             :small_orange_diamond: abs(Х) - модуль числа Х
             :small_orange_diamond: acos(Х) - арккосинус Х
             :small_orange_diamond: asin(Х) - арксинус Х
             :small_orange_diamond: atan(Х) - арктангенс Х
             :small_orange_diamond: atan2(Y, X) - арктангенс Y/X. В радианах. С учетом четверти, в которой находится точка (X, Y)
             :small_orange_diamond: ceil - округление до ближайшего большего числа
             :small_orange_diamond: cos(X) - косинус X (X указывается в радианах)
             :small_orange_diamond: cosh(X) - вычисляет гиперболический косинус
             :small_orange_diamond: degrees(X) - конвертирует радианы в градусы.
             :small_orange_diamond: e - e = 2,718281...
             :small_orange_diamond: exp - экспанента е в степени Х
             :small_orange_diamond: fabs(X) - модуль Х
             :small_orange_diamond: factorial(X) - факториал числа X
             :small_orange_diamond: floor(X) - округление вниз
             :small_orange_diamond: fmod(X, Y) - остаток от деления X на Y
             :small_orange_diamond: frexp(X) - возвращает мантиссу и экспоненту числа
             :small_orange_diamond: hypot(X, Y) - вычисляет гипотенузу треугольника с катетами X и Y
             :small_orange_diamond: log(X, base) - логарифм X по основанию base. Если base не указан, вычисляется натуральный логарифм
             :small_orange_diamond: log10(X) - логарифм X по основанию 10.
             :small_orange_diamond: modf(X) - возвращает дробную и целую часть числа X. Оба числа имеют тот же знак, что и X
             :small_orange_diamond: pi - pi = 3,1415926...
             :small_orange_diamond: pow(Х, У) - Х в степени У. Через pow реализуется извлечение корня любой степени: pow(27, 1/3.0) = 3.0
             :small_orange_diamond: radians(X) - конвертирует градусы в радианы
             :small_orange_diamond: sin(X) - синус X (X указывается в радианах)
             :small_orange_diamond: sinh(X) - вычисляет гиперболический синус
             :small_orange_diamond: sqrt(Х) - корень квадратный из Х
             :small_orange_diamond: tan(X) - тангенс X (X указывается в радианах)
             :small_orange_diamond: tanh(X) - вычисляет гиперболический тангенс
        """, use_aliases=True)

    def calculate(self, expr):
        try:
            x = eval(expr, {"__builtins__": None}, self._safe_dict)
            return u'ответ: %s' % x if x else 'none'
        except Exception as error_msg:
            print('[BotMath] %s' % error_msg)
            return emoji.emojize(u'ошибка вычисления, ты ввел что-то неправильно:heavy_exclamation_mark: Читай справку. :book:', use_aliases=True)


if __name__ == '__main__':
    m = BotMath()
    print(m.calculate(input("y = ")))
