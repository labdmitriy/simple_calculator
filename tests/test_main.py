#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from simple_calculator.main import SimpleCalculator


def test_add_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.add(4, 5)
    assert result == 9


def test_add_three_numbers():
    calculator = SimpleCalculator()
    result = calculator.add(4, 5, 6)
    assert result == 15


def test_add_many_numbers():
    numbers = range(100)
    calculator = SimpleCalculator()
    result = calculator.add(*numbers)
    assert result == 4950


def test_subtract_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.sub(10, 3)
    assert result == 7


def test_mul_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.mul(6, 4)
    assert result == 24


def test_mul_many_numbers():
    numbers = range(1, 10)
    calculator = SimpleCalculator()
    result = calculator.mul(*numbers)
    assert result == 362880


def test_div_two_numbers_float():
    calculator = SimpleCalculator()
    result = calculator.div(13, 2)
    assert result == 6.5


def test_div_by_zero_returns_inf():
    calculator = SimpleCalculator()
    result = calculator.div(5, 0)
    assert result == float('inf')


def test_mul_by_zero_raises_exception():
    calculator = SimpleCalculator()
    with pytest.raises(ValueError):
        calculator.mul(3, 0)


def test_mul_empty_string():
    calculator = SimpleCalculator()
    with pytest.raises(TypeError):
        calculator.mul(3, '')


def test_mul_non_empty_string():
    calculator = SimpleCalculator()
    with pytest.raises(TypeError):
        print(calculator.mul(3, 'a'))


def test_mul_none_value():
    calculator = SimpleCalculator()
    with pytest.raises(TypeError):
        calculator.mul(3, None)


def test_mul_empty_list():
    calculator = SimpleCalculator()
    with pytest.raises(TypeError):
        calculator.mul(3, None)
