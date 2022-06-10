# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
# числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def merger(li):

    if len(li) <= 1:
        return li

    left = merger(li[:len(li) // 2])
    right = merger(li[len(li) // 2:])
    i = 0
    j = 0
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            li[i + j] = left[i]
            i += 1
        else:
            li[i + j] = right[j]
            j += 1
    while len(left) > i:
        li[i + j] = left[i]
        i += 1
    while len(right) > j:
        li[i + j] = right[j]
        j += 1

    return li


a = [random.uniform(0, 50) for _ in range(10)]
print(a)
merger(a)
print(a)
