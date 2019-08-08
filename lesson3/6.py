# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

arr = []
for i in range(10):
    arr.append(int(randint(0, 100)))

print(arr)

min_, max_ = float('inf'), -float('inf')
min_index, max_index = -1, -1

for i in range(len(arr)):
    if min_ > arr[i]:
        min_ = arr[i]
        min_index = i

    if max_ < arr[i]:
        max_ = arr[i]
        max_index = i

print(min_, min_index, max_, max_index)

if max_index < min_index:
    max_index, min_index = min_index, max_index

summ = 0
for i in range(min_index + 1, max_index):
    summ += arr[i]

print(summ)
