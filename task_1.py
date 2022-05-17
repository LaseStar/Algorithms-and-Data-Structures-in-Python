#В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

res = {}

for i in range(2, 10):
    if res.get(i, None) is None:
        res[i] = []

    for j in range(2, 100):
        if j % i == 0:
            res[i].append(j)

for x, y in res.items():
    print(f'Делит на {x}: {len(y)}')
