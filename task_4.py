# Определить, какое число в массиве встречается чаще всего.

import random


def getArray(SIZE=10, MIN_ITEM=1, MAX_ITEM=100):
    return [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


array = getArray(50, 1, 10)
print(f'In: {array}')

freq = {}

for i in array:
    if freq.get(i, None) is None:
        freq[i] = 1
    else:
        freq[i] += 1

res = {
    'value': None,
    'frequency': None
}

for value, frequency in freq.items():
    if res['value'] is None:
        res['value'] = value
        res['frequency'] = frequency
    else:
        if frequency > res['frequency']:
            res['value'] = value
            res['frequency'] = frequency

print(f'Число {res["value"]} встречается в массиве встречается чаще всего  {res["frequency"]} раз')
