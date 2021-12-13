#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Решить поставленную задачу:
написать функцию, вычисляющую среднее геометрическое
своих аргументов a1, a2, ... an
Если функции передается пустой список аргументов,
то она должна возвращать значение  None
"""


def progression(*argument):
    if argument:
        a = 1.0
        for i in argument:
            a *= i
        a = a ** (1 / len(argument))
        return a
    else:
        return None


if __name__ == '__main__':
    arg = list(map(float, input('Введите список аргументов: ').split()))
    print(progression(*arg))