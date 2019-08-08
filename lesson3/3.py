# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import random

arr = []
for i in range(20):
    arr.append(int(random() * 100))

print(arr)

min_ = float('inf')
max_ = -float('inf')
min_index, max_index = -1, -1

for i in range(len(arr)):
    if min_ > arr[i]:
        min_ = arr[i]
        min_index = i

    if max_ < arr[i]:
        max_ = arr[i]
        max_index = i

print(f' меняем {min_} и {max_}')
arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
print(arr)
