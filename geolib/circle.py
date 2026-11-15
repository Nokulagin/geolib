"""Модуль для простых вычислений, связанных с кругом.

Функции:
- area(radius): возвращает площадь круга
- perimeter(radius): возвращает длину окружности
"""

from math import pi


def area(radius: float) -> float:
    """Площадь круга: π * r^2"""
    return pi * radius**2


def perimeter(radius: float) -> float:
    """Длина окружности (периметр): 2 * π * r"""
    return 2 * pi * radius
