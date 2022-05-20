#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
import timeit
import cProfile


def min_max(size):
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
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


print(timeit.timeit('min_max(10)', number=1000, globals=globals()))                         #0.22929450000083307
print(timeit.timeit('min_max(100)', number=1000, globals=globals()))                        #3.7979037999994034
print(timeit.timeit('min_max(1000)', number=1000, globals=globals()))                       #30.455246200001056
print(timeit.timeit('min_max(10000)', number=1000, globals=globals()))                      #34.803127699999095

cProfile.run('min_max(10_000)')

#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.052    0.052 <string>:1(<module>)
# 10000    0.006    0.000    0.009    0.000 random.py:239(_randbelow_with_getrandbits)
# 10000    0.011    0.000    0.023    0.000 random.py:292(randrange)
# 10000    0.004    0.000    0.027    0.000 random.py:366(randint)
#     1    0.005    0.005    0.052    0.052 task_1.py:8(min_max)
#     1    0.004    0.004    0.032    0.032 task_1.py:9(<listcomp>)
# 30000    0.003    0.000    0.003    0.000 {built-in method _operator.index}
#     1    0.000    0.000    0.052    0.052 {built-in method builtins.exec}
#     2    0.015    0.008    0.015    0.008 {built-in method builtins.print}
# 10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 13124    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
