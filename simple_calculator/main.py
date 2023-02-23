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

    def avg(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if ut is not None and number > ut:
                continue
            if lt is not None and number < lt:
                continue
            count += 1
            total += number

        if count == 0:
            return 0
        else:
            return total / count
