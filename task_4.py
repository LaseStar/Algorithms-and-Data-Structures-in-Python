#Определить, является ли год, который ввел пользователь, високосным или не високосным.
print('Введите год')
year = int(input())

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('Да')
else:
    print('Нет')
