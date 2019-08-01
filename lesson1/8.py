# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = int(input('Введите год: '))


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


print(is_leap_year(year))
