import timeit
import cProfile


def prime(num):
    count = 1
    current_prime = 2

    while count < num:
        current_prime += 1

        for i in range(2, int(current_prime ** 0.5) + 1):
            if current_prime % i == 0:
                break
        else:
            count += 1

    return current_prime


search_position = int(input('Введите позицию искомого числа: '))
print(prime(search_position))

print(timeit.timeit('prime(10)', number=1000, globals=globals()))           #0.024506799999471696
print(timeit.timeit('prime(100)', number=1000, globals=globals()))          #0.42961300000024494
print(timeit.timeit('prime(200)', number=1000, globals=globals()))          #1.0380904000003284
print(timeit.timeit('prime(300)', number=1000, globals=globals()))          #1.7613972000008289

cProfile.run('prime(300)')

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 task_5.py:5(prime)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
