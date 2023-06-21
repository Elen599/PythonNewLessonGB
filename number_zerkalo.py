# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

A = 1
B = 10
C = 100
minDig = 1
maxDig = 999
while True:
    n = int(input('введите число от 1 до 999 : '))
    if minDig <= n <= maxDig: break
if n // A < B : x = n * n
elif n // B < B : x = (n % B) * (n//B)
elif n // C < B : x = (n % B) * C + (((n % C) // B) * B) + (n // C)
print(n,' : ',x)

################################  2 вариант  ############################
# import constant
#
# def check_number(num):
#     if num > constant.low_line and num < constant.high_line:
#         l = len(str(num))
#         num_mirror = constant.zero
#         if l == constant.len_three:
#             number = num
#             while num > constant.zero:
#                 dig = num % constant.num_dec
#                 num = num // constant.num_dec
#                 num_mirror = num_mirror * constant.num_dec
#                 num_mirror = num_mirror + dig
#             return f"зеркальное число {number} - " + str(num_mirror)
#         elif l == constant.len_two:
#             dig = num % constant.num_dec
#             num = num // constant.num_dec
#             num_mult = num * dig
#             return f"произведение {num} и {dig} = " + str(num_mult)
#         else:
#             n_sq = num ** constant.square
#             return f"квадрат числа {num} = " + str(n_sq)
#     else:
#         return f"число {num} не из диапазона, запросите новое число"
#
# def Main():
#     number = int(input('Введите число от 1 до 999 - '))
#     print(check_number(number))
#
# Main()