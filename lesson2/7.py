# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


def test_equality(n):
    summ = 0

    for i in range(1, n + 1):
        summ += i
    print(f'1+2+...+n = {summ}')

    test_summ = n * (n + 1) / 2
    print(f'n(n+1)/2 = {test_summ}')

    return summ == test_summ


print(test_equality(int(input('Введите размер последовательности: '))))
