#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
import sys


def size(data, total_size=0):
    total_size += sys.getsizeof(data)
    if hasattr(data, '__iter__'):
        if hasattr(data, 'items'):
            for key, value in data.items():
                total_size += size(key)
                total_size += size(value)
        elif not isinstance(data, str):
            for item in data:
                total_size += size(item)
    return total_size


def min_max(size_):
    array = [random.randint(size_ * -10, size_ * 10) for _ in range(size_)]

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

    return print(f'Конечный размер списка в памяти {size(array)=}')


min_max(10)                         #Конечный размер списка в памяти size(array)=464
min_max(100)                        #Конечный размер списка в памяти size(array)=3716
min_max(1000)                       #Конечный размер списка в памяти size(array)=36856
min_max(10_000)                     #Конечный размер списка в памяти size(array)=365176
