# Задача1. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:   - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
n = int(input('Введите количество элементов списка: '))
num_list = []
for i in range(n):
    num_list.append(randint(0, 10))
print(num_list)
sum_num = 0
for i in range(len(num_list)):
    if i % 2 != 0:
        sum_num += num_list[i]
    else:
        continue    
print(sum_num)        
