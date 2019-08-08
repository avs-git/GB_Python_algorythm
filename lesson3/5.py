# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
from random import randint

arr = []
for i in range(20):
    arr.append(int(randint(-10, 10)))

print(arr)

max_sub = -float('inf')

for i in arr:
    if max_sub < i < 0:
        max_sub = i

print(max_sub)
