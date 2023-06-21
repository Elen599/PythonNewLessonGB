# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
#     from random import randint
#     num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
num = randint(0, 10)
count = 1
while count < 10:
    n = int(input('число :'))
    if n == num :
        print('угадал')
        break
    elif n > num : print('мое число меньше. ', count+1, ' попытка')
    else : print('мое число больше ',count+1, ' попытка')
    count +=1
print('мое число : ', num)

##############  вариант  #############
# from random import randint
#
# def game():
#     num = randint(0, 1000)
#     print(f'загаданное число {num}')
#     for i in range(1, 11):
#         num_check = int(input(f'Попытка № {i} Введите число - '))
#         if num_check > num:
#             print('больше')
#         elif num_check < num:
#             print('меньше')
#         elif num_check == num:
#             return 'угадали'
#     return 'не угадали'
#
# def Main():
#     print(game())