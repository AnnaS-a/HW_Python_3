# Задача5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#  [Негафибоначчи]
import copy
k = int(input('Введите число: '))

def fibon(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b  
res = list(fibon(k+1))

arr = list(copy.deepcopy(res))
for i in range(len(arr)):
    if i % 2 != 0:
        continue  
    elif i % 2 == 0:
        arr[i] = arr[i] * (-1) 
arr.reverse()
res = res[1:]

fibon2 = arr + res
print(f'для k = {k} =>', fibon2)    
            
                