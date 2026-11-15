"""Площадь и периметр треугольника по трём сторонам."""

from math import sqrt


def area(a: float, b: float, c: float) -> float:
    """Вернуть площадь треугольника по формуле Герона."""
    half_perimeter = perimeter(a, b, c) / 2
    return sqrt(half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c))


def perimeter(a: float, b: float, c: float) -> float:
    return a + b + c
