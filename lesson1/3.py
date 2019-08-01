# 3. По введенным пользователем координатам двух точек вывести уравнение
# прямой вида y=kx+b, проходящей через эти точки.


x1, y1, x2, y2 = list(
    map(lambda x: int(x.strip()), input('Введите координаты x1, y1, x2, y2 через запятую: ').split(',')))


def get_equation(x1, y1, x2, y2):
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2

    return f'y = {round(k, 2)}x + {round(b, 2)}'


print(get_equation(x1, y1, x2, y2))
