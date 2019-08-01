# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

num = int(input('Введите номер буквы: '))


def get_letter(num):
    if not (0 < num < 27):
        return f'в алфавите нет столько букв'

    return chr(ord('a') + num - 1)


print(get_letter(num))
