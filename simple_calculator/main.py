# -*- coding: utf-8 -*-

from functools import reduce
from numbers import Number
from operator import mul


class SimpleCalculator:
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        if not all(isinstance(arg, Number) for arg in args):
            raise TypeError
        elif any(arg == 0 for arg in args):
            raise ValueError
        return reduce(mul, args)

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return float('inf')
