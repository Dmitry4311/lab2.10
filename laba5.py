#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def min_max(*args):
    if not args:
        return None

    multi = 1

    maximum = args[0]
    max_ind = 0

    minimum = args[0]
    min_ind = 0

    for i, item in enumerate(args):
        if item > maximum:
            maximum = item
            max_ind = i
        if item < minimum:
            minimum = item
            min_ind = i
    for i in args[min_ind:max_ind]:
        multi *= i
    return multi


if __name__ == '__main__':
    print("Введите список аргументов: ")
    arg = list(map(float, input().split()))
    print(min_max(*arg))
