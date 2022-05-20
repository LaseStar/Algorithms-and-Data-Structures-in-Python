import random
import timeit
import cProfile


def min_max(size):
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
    print(f'Входные данные: {array}')

    min_ = 0
    max_ = 0
    for i in range(len(array)):
        if array[i] < array[min_]:
            min_ = i
        elif array[i] > array[max_]:
            max_ = i
    array[min_], array[max_] = array[max_], array[min_]
    print(f'Выходные данные: {array}')


print(timeit.timeit('min_max(10)', number=1000, globals=globals()))                 #0.08650119999947492
print(timeit.timeit('min_max(100)', number=1000, globals=globals()))                #3.8065935999984504
print(timeit.timeit('min_max(1000)', number=1000, globals=globals()))               #30.391868200000317
print(timeit.timeit('min_max(10000)', number=1000, globals=globals()))              #32.49645059999966

cProfile.run('min_max(10_000)')

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.076    0.076 <string>:1(<module>)
#     10000    0.010    0.000    0.014    0.000 random.py:239(_randbelow_with_getrandbits)
#     10000    0.021    0.000    0.040    0.000 random.py:292(randrange)
#     10000    0.006    0.000    0.046    0.000 random.py:366(randint)
#         1    0.004    0.004    0.076    0.076 task_3.py:6(min_max)
#         1    0.007    0.007    0.053    0.053 task_3.py:7(<listcomp>)
#     30000    0.004    0.000    0.004    0.000 {built-in method _operator.index}
#         1    0.000    0.000    0.076    0.076 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         2    0.018    0.009    0.018    0.009 {built-in method builtins.print}
#     10000    0.002    0.000    0.002    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     13062    0.003    0.000    0.003    0.000 {method 'getrandbits' of '_random.Random' objects}


"""
Во всех случаях наблюдается линейная сложность. В во втором случая мы использовали вещественные числа, 
в первом целые, в третьем не много оптимизировали код и судя по замерам он отработал быстрее. 
"""
