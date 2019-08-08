# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

numbers = [_ for _ in range(2, 100)]
mods = [_ for _ in range(2, 10)]
numbers_mods = {}

counter = 0
for mod in mods:
    numbers_mods[mod] = 0
    for number in numbers:
        if not number % mod:
            numbers_mods[mod] += 1

for key, value in numbers_mods.items():
    print(f'на {key} делится {value} элементов')
