# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# import os
# os.system('cls')
# a = [] 
# n = int(input("Введите число N: "))  
# m = 1
# while m < n:
#     for i in range(n):  
#         import math
#         new_element = math.factorial(m)
#         a.append(new_element)
#         m = m + 1
# print("Пусть N =", n, "тогда ->", a)

import os
os.system('cls')

from math import factorial

number = int(input("Введите число N: "))

print(f'Пусть N = {number}, тогда -> {list(map(lambda x: ((x == 1) and 1) or x * factorial(x - 1), list(range(1, number+1))))}')

