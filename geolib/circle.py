"""Модуль для вычисления площади и длины окружности

Функции:
- area(radius: float) -> float
- perimeter(radius: float) -> float
"""

from math import pi


def area(radius: float) -> float:
    """Вернуть площадь круга с заданным радиусом.

    Формула: pi * radius**2
    """
    return pi * radius ** 2


def perimeter(radius: float) -> float:
    """Вернуть длину окружности с заданным радиусом.

    Формула: 2 * pi * radius
    """
    return 2 * pi * radius
