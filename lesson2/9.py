# 9. Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр

num1, num2, num3 = map(lambda _: int(_.strip()), input('Введите 3 числа через запятую: ').split(','))


def get_max_sum(num1, num2, num3):
    s1, s2, s3 = get_sum_digits(num1), get_sum_digits(num2), get_sum_digits(num3)
    max_sum, max_num = s1, num1

    if s2 > s1 and s2 > s3:
        max_sum, max_num = s2, num2

    if s3 > s1 and s3 > s2:
        max_sum, max_num = s3, num3

    return f'самая большая сумма цифр в {max_num}: {max_sum}'


def get_sum_digits(num):
    summ = 0
    while num > 0:
        summ += num % 10
        num = num // 10

    return summ


print(get_max_sum(num1, num2, num3))
