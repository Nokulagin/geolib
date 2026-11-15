# geolib

Небольшая Python-библиотека для расчёта площадей и периметров плоских фигур. Требуется Python 3.10 или новее.

```bash
python -m pip install .
```

```python
from geolib import circle, rectangle, square, triangle

print(square.area(4))                 # 16
print(rectangle.perimeter(3, 5))      # 16
print(triangle.area(3, 4, 5))          # 6.0
print(circle.perimeter(3))
```

| Модуль | Аргументы `area()` и `perimeter()` |
|---|---|
| `circle` | Радиус `radius`. Площадь круга равна `πr²`, длина окружности — `2πr`. |
| `rectangle` | Ширина `width` и высота `height`. |
| `square` | Длина стороны `side`. |
| `triangle` | Длины трёх сторон `a`, `b`, `c`. |

Передавай положительные размеры в одинаковых единицах. Для треугольника сумма двух любых сторон должна быть больше третьей.
