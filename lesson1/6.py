# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

num = int(input('Введите номер буквы: '))


def get_letter(num):
    return chr(ord('a') + num - 1) if 0 < num < 27 else f'в алфавите нет столько букв'


print(get_letter(num))
