# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
from random import random

begin, end = list(map(lambda x: x.strip(), input('Введите пределы min,max через запятую: ').split(',')))

if end < begin:
    begin, end = end, begin


def get_random_num(start, stop):
    return int(random() * (stop - start) + start)


def get_random_char(start, stop):
    return chr(get_random_num(ord(start), ord(stop)))


def get_random_in_range(start, stop):
    # если один из пределов не число - рассматриваем оба предела как символы
    if not start.isnumeric() or not stop.isnumeric():
        return get_random_char(start, stop)

    return get_random_num(int(start), int(stop))


print(get_random_in_range(begin, end))
