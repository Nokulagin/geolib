"""Площадь круга и длина окружности по радиусу."""

from math import pi


def area(radius: float) -> float:
    """Вернуть площадь круга."""
    return 2 * pi * radius**2


def perimeter(radius: float) -> float:
    """Вернуть длину окружности."""
    return pi * radius
