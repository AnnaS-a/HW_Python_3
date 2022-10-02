# Задача4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:   - 45 -> 101101    - 3 -> 11      - 2 -> 10
from math import remainder
from unicodedata import decimal

num = int(input('Введите число: '))
binary_num = ''
while num > 0:
    binary_num = str(num % 2) + binary_num
    num = num // 2
    
print(binary_num)
