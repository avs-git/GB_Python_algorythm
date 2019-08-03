# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под
# номером 32 и заканчивая 127-м включительно. Вывод выполнить в табличной
# форме: по десять пар "код-символ" в каждой строке.


def char_table(start, stop):
    row = ''
    col = 0
    for i in range(start, stop):
        row += f'{str(i):<3} {chr(i):<3}'
        col += 1
        if not col % 10:
            row += '\n'

    return row


print(char_table(32, 127))
