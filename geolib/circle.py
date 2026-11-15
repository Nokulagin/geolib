"""Модуль geolib.circle

Функции:
- area(radius): возвращает площадь круга
- perimeter(radius): возвращает длину окружности
"""

from math import pi


def area(radius: float) -> float:
    """Возвращает площадь круга: pi * r^2"""
    return pi * radius**2


def perimeter(radius: float) -> float:
    """Возвращает длину окружности: 2 * pi * r"""
    return 2 * pi * radius
