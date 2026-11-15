"""Круговые утилиты: площадь и периметр (длина окружности)."""

from math import pi


def area(radius: float) -> float:
    """Вычисляет площадь круга: pi * radius**2"""
    return pi * radius**2


def perimeter(radius: float) -> float:
    """Вычисляет длину окружности: 2 * pi * radius"""
    return 2 * pi * radius
