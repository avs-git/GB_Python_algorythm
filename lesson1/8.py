# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = int(input('Введите год: '))


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True

    return False


print(is_leap_year(year))
