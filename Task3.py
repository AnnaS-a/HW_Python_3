# Задача3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.
# Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
num_list = []
for i in range(7):
    num = round(random.random()* 10, 2)
    num_list.append(num)
print(num_list)

for i in range(len(num_list)):
    num_list[i] = round((num_list[i] % 1), 2)
    
num_list.sort()
res = num_list[-1] - num_list[0]
print(f'разниц между максимальным и минимальным значением дробной части элементов', round(res, 2))
  
