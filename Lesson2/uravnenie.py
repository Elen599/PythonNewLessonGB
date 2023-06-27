# Напишите программу, которая решает квадратные уравнения даже если
# дискриминант отрицательный.
# Используйте комплексные числа
# для извлечения квадратного корня.

import math
import cmath

def quadratic_equation(a, b, c):
    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = %.3f" % discr)

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = %.3f \nx2 = %.3f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        print("x = %.3f" % x)
    elif discr < 0:
        x1 = complex((-b + cmath.sqrt(discr)) / (2 * a))
        x2 = complex((-b - cmath.sqrt(discr)) / (2 * a))
        print(f'x1 = {x1} \nx2 = {x2}')

def Main():
    print("Введите коэффициенты для уравнения")
    print("ax^2 + bx + c = 0:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    quadratic_equation(a, b, c)

Main()