# 4. Определить, какое число в массиве встречается чаще всего.
from random import randint

arr = []
for i in range(20):
    arr.append(int(randint(0, 5)))

quant = {}

for num in arr:
    if not quant.get(num):
        quant[num] = 0

    quant[num] += 1

max_ = 0
number = -1
for key, value in quant.items():
    if max_ < value:
        max_ = value
        number = key

print(arr)
print(f'в массиве наибольшее количество повторений - {max_} у числа {number}')