# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


def count_digits(test, number, count=0):
    if number == 0:
        return count

    if test == number % 10:
        count += 1

    return count_digits(test, number // 10, count)


num = int(input('Введите последовательность чисел: '))
test = int(input('Введите цифру для поиска: '))
print(f'количество вхождений {test} в {num}: {count_digits(test, num)}')
