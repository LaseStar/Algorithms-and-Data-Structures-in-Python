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
    array = [random.randrange(size_ * -10, size_ * 10) for _ in range(size_)]

    min_ = 0
    max_ = 0
    for i in range(len(array)):
        if array[i] < array[min_]:
            min_ = i
        elif array[i] > array[max_]:
            max_ = i
    array[min_], array[max_] = array[max_], array[min_]
    return print(f'Конечный размер списка в памяти {size(array)=}')


min_max(10)                     #Конечный размер списка в памяти size(array)=460
min_max(100)                    #Конечный размер списка в памяти size(array)=3720
min_max(1000)                   #Конечный размер списка в памяти size(array)=36856
min_max(10_000)                 #Конечный размер списка в памяти size(array)=36856

"""
По трем задачам видно что вещественные занимаею меньше всего памяти, 
целые больше
Windows 10 x64
Python 3.10
"""
