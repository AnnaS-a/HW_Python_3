# Задача2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:  - [2, 3, 4, 5, 6] => [12, 15, 16];  - [2, 3, 5, 6] => [12, 15]

from random import random

num_list = []
for i in range(7):
    num = int(random() * 10)
    num_list.append(num)

mult_list = []
for i in range(len(num_list)//2 + 1):
    d = num_list[i] * num_list[-1-i]
    i += 1
    mult_list.append(d)
   
print(num_list, f'=>', mult_list)
