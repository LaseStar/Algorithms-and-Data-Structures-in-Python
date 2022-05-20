#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
import timeit
import cProfile


def min_max(size):
    array = [random.uniform(size * -10, size * 10) for _ in range(size)]
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

    return print(f'Выходные данные: {array}')


print(timeit.timeit('min_max(10)', number=1000, globals=globals()))                 #0.4696241000019654
print(timeit.timeit('min_max(100)', number=1000, globals=globals()))                #10.101433600000746
print(timeit.timeit('min_max(1000)', number=1000, globals=globals()))               #30.65574370000104
print(timeit.timeit('min_max(10000)', number=1000, globals=globals()))              #42.80627430000095

cProfile.run('min_max(10_000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.047    0.047 <string>:1(<module>)
#     10000    0.004    0.000    0.005    0.000 random.py:546(uniform)
#         1    0.017    0.017    0.047    0.047 task_2.py:8(min_max)
#         1    0.004    0.004    0.008    0.008 task_2.py:9(<listcomp>)
#         1    0.000    0.000    0.047    0.047 {built-in method builtins.exec}
#         2    0.022    0.011    0.022    0.011 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     10000    0.001    0.000    0.001    0.000 {method 'random' of '_random.Random' objects}
