#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random


def getArray(SIZE=10, MIN_ITEM=1, MAX_ITEM=100):
    return [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


array = getArray()
print(f'Входные данные: {array}')

last = {
    'min': {
        'index': 0,
        'value': array[0]
    },
    'max': {
        'index': 0,
        'value': array[0]
    },
}

for item, value in enumerate(array):
    if value < last['min']['value']:
        last['min']['value'] = value
        last['min']['index'] = item

    if value > last['max']['value']:
        last['max']['value'] = value
        last['max']['index'] = item

min_ = last['min']['index']
max_ = last['max']['index']

array[min_], array[max_] = array[max_], array[min_]

print(f'Выходные данные: {array}')
