# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

Enterprise = namedtuple('Enterprise', 'name q1 q2 q3 q4 total')

enterprises_count = int(input('Введите количество предприятий: '))

enterprises = []
total_income = 0

for i in range(enterprises_count):
    name = input(f'Введите имя {i + 1} предприятия: ')
    q1 = float(input(f'Введите доход предприятия {i + 1} за 1 кв.: '))
    q2 = float(input(f'Введите доход предприятия {i + 1} за 2 кв.: '))
    q3 = float(input(f'Введите доход предприятия {i + 1} за 3 кв.: '))
    q4 = float(input(f'Введите доход предприятия {i + 1} за 4 кв.: '))
    total = q1 + q2 + q3 + q4
    total_income += total
    enterprises.append(Enterprise(name, q1, q2, q3, q4, total))

average_income = total_income / enterprises_count

print(f'Средняя прибыль: {average_income}')

above_average_income = []
below_average_income = []

for enterprise in enterprises:
    if enterprise.total < average_income:
        below_average_income.append(enterprise.name)
    else:
        above_average_income.append(enterprise.name)

print('Прибыль выше среднего у:')
print(*above_average_income, sep='\n')
print('Прибыль ниже среднее у:')
print(*below_average_income, sep='\n')
