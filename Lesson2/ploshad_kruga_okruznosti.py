# Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import math
import decimal

decimal.getcontext().prec = 50
from decimal import Decimal
myPi = Decimal(math.pi)
diam = Decimal(input('введите диаметр : '))
print(f'Длина окружности = {myPi*(diam)}, Площадь круга {myPi*(diam/2 * diam/2)} ')

############################################## 2 вариант ##########
from decimal import *
import math as M

def square_Сircle (diametr):
    sq_Сircle = Decimal(M.pi * ((diametr/2) ** 2))
    return sq_Сircle

def length_Сircle (diametr):
    len_Сircle = Decimal(M.pi * diametr)
    return len_Сircle

def Main():
    diametr = float(input('Введите диаметр круга - '))
    if diametr <= 1000:
        print('Площадь круга = ', square_Сircle(diametr))
        print('Длина круга = ', length_Сircle(diametr))
    else:
        print('Диаметр не должен превышать 1000 у.е.')

Main()