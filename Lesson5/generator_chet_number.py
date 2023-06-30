# ГЕНЕРАТОР ЧЕТНЫХ ЧИСЕЛ

# Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.


print(f'{list(i for i in range(2, 100, 2) if sum(int(j) for j in str(i) )!=8)}')


#################### 2  вариант ############################
#import random; print([random.randrange(2, 100, 2) for i in range(100) if sum(int(j) for j in str(i)) != 8])


#################### 3  вариант ############################

# print([i for i in range(2, 100, 2) if sum(int(j) for j in str(i)) != 8])