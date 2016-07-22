#!/usr/bin/env python
# -*- coding: utf8 -*-
from math import *
SAVE_LIST = [
    'math', 'acos', 'asin', 'atan', 'atan2', 'ceil', 'factorial'
    'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod',
    'frexp', 'hypot', 'ldexp', 'log', 'log10', 'modf', 'pi',
    'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh'
]


class BotMath(object):
    def __init__(self):
        self._safe_dict = dict([(k, globals().get(k, None)) for k in SAVE_LIST])
        self._safe_dict['abs'] = abs

    @staticmethod
    def get_help():
        return u"""
            Ключевые литералы и их особенности для математики бота:
             * Сложение, Вычитание, Умножение, Разность: \'+\' \'-\' \'*\' \'/\'
             * Дробные числа используют символ \'.\': 2.5
             * Приоритеты операций определяются по правилам математики. Так же можно использовать круглые скобки
             * Особенности деления:
             \tПроисходит деление либо целых чисел (результат целое), либо вещественных.
             \tНапример: 5/2 = 2, 5/2.0 = 2.5

            Доступные функции:
             * abs(Х) - модуль числа Х
             * acos(Х) - арккосинус Х
             * asin(Х) - арксинус Х
             * atan(Х) - арктангенс Х
             * atan2(Y, X) - арктангенс Y/X. В радианах. С учетом четверти, в которой находится точка (X, Y)
             * ceil - округление до ближайшего большего числа
             * cos(X) - косинус X (X указывается в радианах)
             * cosh(X) - вычисляет гиперболический косинус
             * degrees(X) - конвертирует радианы в градусы.
             * e - e = 2,718281...
             * exp - экспанента е в степени Х
             * fabs(X) - модуль Х
             * factorial(X) - факториал числа X
             * floor(X) - округление вниз
             * fmod(X, Y) - остаток от деления X на Y
             * frexp(X) - возвращает мантиссу и экспоненту числа
             * hypot(X, Y) - вычисляет гипотенузу треугольника с катетами X и Y
             * log(X, base) - логарифм X по основанию base. Если base не указан, вычисляется натуральный логарифм
             * log10(X) - логарифм X по основанию 10.
             * modf(X) - возвращает дробную и целую часть числа X. Оба числа имеют тот же знак, что и X
             * pi - pi = 3,1415926...
             * pow(Х, У) - Х в степени У. Через pow реализуется извлечение корня любой степени: pow(27, 1/3.0) = 3.0
             * radians(X) - конвертирует градусы в радианы
             * sin(X) - синус X (X указывается в радианах)
             * sinh(X) - вычисляет гиперболический синус
             * sqrt(Х) - корень квадратный из Х
             * tan(X) - тангенс X (X указывается в радианах)
             * tanh(X) - вычисляет гиперболический тангенс
        """

    def calculate(self, expr):
        try:
            x = eval(expr, {"__builtins__": None}, self._safe_dict)
            return u'ответ: %s' % x if x else 'none'
        except:
            return u'ошибка вычисления, ты ввел что-то неправильно. Читай справку.'


if __name__ == '__main__':
    m = BotMath()
    print m.calculate(raw_input("y = "))
