# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
from random import randint

# arr = []
# for i in range(20):
#     arr.append(int(randint(0, 10)))

arr = [1, 1, 1, 8, 6, 7, 9, 9, 4, 8, 6, 5, 10, 2, 4, 9, 10, 10, 0, -1]
print(arr)

min_1, min_2 = float('inf'), float('inf')
min_1_index, min_2_index = -1, -1

for i in range(len(arr)):
    if min_1 > arr[i] and i != min_2_index:
        # позволяет не потерять значения при расположении минимальных элементов последними. Экономит один цикл
        min_2 = min_1

        min_1 = arr[i]
        min_1_index = i

    if min_2 > arr[i] and i != min_1_index:
        min_2 = arr[i]
        min_2_index = i

print(f'min1 = {min_1}, min2 = {min_2}')
