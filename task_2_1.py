import timeit
import cProfile


def prime(num):
    size = num ** 2 + 3
    a = [0] * size  # создание массива с n количеством элементов

    for i in range(size):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < size:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < size:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    # запоняем простыми числами новый список
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    return b[num-1]


search_position = int(input('Введите позицию искомого числа: '))
print(prime(search_position))

print(timeit.timeit('prime(10)', number=1000, globals=globals()))               #0.03318429999944783
print(timeit.timeit('prime(100)', number=1000, globals=globals()))              #4.162846100000024
print(timeit.timeit('prime(200)', number=1000, globals=globals()))              #17.394551299999875
print(timeit.timeit('prime(300)', number=1000, globals=globals()))              #38.84943739999926

cProfile.run('prime(300)')

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.043    0.043 <string>:1(<module>)
#         1    0.041    0.041    0.042    0.042 task_4.py:5(prime)
#         1    0.000    0.000    0.043    0.043 {built-in method builtins.exec}
#      8714    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
