from math import pi


def area(radius: float) -> float:
    """Return the area of a circle with the given radius.

    Formula: area = pi * radius**2
    """
    return pi * radius ** 2


def perimeter(radius: float) -> float:
    """Return the circumference (perimeter) of a circle with the given radius.

    Formula: perimeter = 2 * pi * radius
    """
    return 2 * pi * radius
