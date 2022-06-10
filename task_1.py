# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный
# случайными числами на промежутке[-100;100).Выведите на экран исходный и отсортированный массивы.
import random


def bubble(li):
    n = 1

    while n < len(li):
        sort_comp = True
        for i in range(len(li) - n):
            if li[i] < li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
                sort_comp = False

        if sort_comp:
            break

        n += 1
        print(li)


a = [random.randrange(-100, 100) for _ in range(10)]
print(a)
bubble(a)
print(a)
