# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

hex_array_1 = list(input('Введите первое шестнадцатеричное число: ').upper())
hex_array_2 = list(input('Введите второе шестнадцатеричное число: ').upper())

hex_deque_1 = deque(hex_array_1)
hex_deque_2 = deque(hex_array_2)
hex_deque_1.reverse()
hex_deque_2.reverse()

if len(hex_deque_2) > len(hex_deque_1):
    x = hex_deque_2
    y = hex_deque_1
else:
    y = hex_deque_2
    x = hex_deque_1


def get_hex_sum(a, b):
    digits = '0123456789ABCDEF'
    a_digit_index = digits.index(a)
    b_digit_index = digits.index(b)

    index_sum = a_digit_index + b_digit_index

    result = [digits[index_sum // 16], digits[index_sum % 16]]

    return result


raw_result = deque()
in_mind = '0'

for i in range(len(x)):
    a = x[i]

    if len(y) <= i:
        b = in_mind
    else:
        b = y[i]

    sum_of_position_i = get_hex_sum(a, b)
    sum_considering_in_mind = get_hex_sum(sum_of_position_i[1], in_mind)

    in_mind = sum_of_position_i[0]

    if len(y) <= i:
        position_digit = sum_of_position_i[1]
    else:
        position_digit = sum_considering_in_mind[1]

    raw_result.append(position_digit)

    is_last_digit = i == len(x) - 1

    if is_last_digit:
        if sum_considering_in_mind[0] == '1':
            raw_result.append(sum_considering_in_mind[0])
        elif in_mind == '1':
            raw_result.append(in_mind)

raw_result.reverse()
result = list(raw_result)
print(result)
