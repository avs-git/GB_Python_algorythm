# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def count_odd_even_recursion(num, even=0, odd=0):
    if num == 0:
        return f'чётных: {even}, нечётных {odd}'

    if num % 10 % 2:
        odd += 1
    else:
        even += 1

    return count_odd_even_recursion(num // 10, even, odd)


def count_odd_even_loop(num):
    even, odd = 0, 0

    while num > 0:
        if num % 10 % 2:
            odd += 1
        else:
            even += 1

        num = num // 10

    return f'чётных: {even}, нечётных {odd}'


number = int(input('Введите число: '))
print(f'рекурсия: {count_odd_even_recursion(number)}')
print(f'цикл: {count_odd_even_loop(number)}')
