# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать
# ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.


# from random import random, randint

M = 5
N = 4
a = []
for i in range(N):
    b = []
    row_sum = 0
    for j in range(M):
        # b.append(randint(0, 10))
        b.append(int(input(f'{i}:{j} = ')))
    a.append(b)

for i in range(N):
    row_sum = 0
    for j in range(M):
        print(f'{a[i][j]:<3}', end=' ')
        row_sum += a[i][j]
    print(' |', row_sum)


