# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random


def getArray(SIZE=10, MIN_ITEM=1, MAX_ITEM=100):
    return [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


array = getArray(10, -100, 100)
print(f'In: {array}')

maxNegative = None
pos = None

for index, i in enumerate(array):
    if i < 0:
        if maxNegative is None:
            maxNegative = i
            pos = index
        elif maxNegative < i:
            maxNegative = i
            pos = index

print(f':Максимальный отрицательный элемент {maxNegative}, его позиция: {pos}')
