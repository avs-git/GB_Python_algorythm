# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.


def sum_n(n):
    num = 1
    result = 0

    while n > 0:
        result += num
        num = - num / 2
        n -= 1

    return result


def sum_n_recursion(n, elem=1.0, result=0.0):
    if n == 0:
        return result

    return sum_n_recursion(n - 1, - elem / 2, result + elem)


number = int(input('Количество элементов: '))
print(sum_n(number))
print(sum_n_recursion(number))
