# -*- coding: utf-8 -*-

from functools import reduce


class SimpleCalculator:
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        return reduce(lambda x, y: x * y, args)
