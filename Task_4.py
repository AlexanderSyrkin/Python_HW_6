# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# X_1 = int(input("Введите первое значение А по Х: "))
# Y_1 = int(input("Введите второе значение А по Y: "))
# X_2 = int(input("Введите первое значение В по Х: "))
# Y_2 = int(input("Введите первое значение В по Y: "))

# dist_in_space = ((X_2-X_1)**2 + (Y_2-Y_1)**2)**0.5
# print("A (",(X_1),",",(Y_1),"); ", "B (",(X_2),",",(Y_2),") -> ","%.2f" % dist_in_space, sep="")

import os
os.system('cls')

from functools import reduce
dot_1 = list(map(int, input('Введите две координаты первой точки A, через пробел: ').split())) 
dot_2 = list(map(int, input('Введите две координаты второй точки B, через пробел: ').split()))
def dot_range(dot_1, dot_2):
     rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot_1, dot_2))))
     return round(rng, 2)
print('Расстояние между точками в 2D пространстве =', dot_range(dot_1, dot_2))
