# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.


def reverse_number(num):
    result = ''
    while num > 0:
        result += str(num % 10)
        num = num // 10

    return result

print(reverse_number(int(input('Число: '))))
