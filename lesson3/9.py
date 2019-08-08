# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random, randint

M = 5
N = 4
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(randint(0, 10))
    print(b)
    a.append(b)

min_cols = []

for j in range(M):
    min_ = float('inf')

    for i in range(N):
        if min_ > a[i][j]:
            min_ = a[i][j]

    min_cols.append(min_)

print()
print(min_cols)

max_ = -float('inf')
for num in min_cols:
    if max_ < num:
        max_ = num

print(max_)

