# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print
# файл constant.py содержит следующие переменные

vis_year_mult_four_h = 400     # год, номер которого кратен 400, — високосный
vis_year_mult_one_h = 100     # остальные года, номер которых кратен 100, — невисокосные;
vis_year_mult_four = 4         # остальные года, номер которых кратен 4, — високосные;

low_line = 1
high_line = 999
len_three = 3
len_two = 2
num_dec = 10
square = 2

zero = 0

def check_year(y):
    if (y % vis_year_mult_four == zero) \
            and (y % vis_year_mult_one_h != zero) \
            or (y % vis_year_mult_four_h == zero):
        return "Данный год является високостный"
    else:
        return "Данный год не является високостным"

def Main():
    year = float(input('Введите год - '))
    print(check_year(year))

Main()