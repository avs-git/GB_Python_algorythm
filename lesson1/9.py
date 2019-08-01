# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

num1, num2, num3 = list(map(lambda x: int(x.strip()), input('введите 3 числа через запятую: ').split(',')))


def get_middle(a, b, c):
    return a if b < a < c or c < a < b \
        else b if a < b < c or c < b < a \
        else c if a < c < b or b < c < a \
        else 'нет среднего'


print(get_middle(num1, num2, num3))
