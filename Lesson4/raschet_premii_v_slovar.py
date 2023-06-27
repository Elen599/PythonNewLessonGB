# Расчет премии 
# 
# Функция принимает на вход три списка одинаковой длины:
# имена str, 
# ставка int, 
# премия str 
# с указанием процентов вида «10.25%».
# Вернуть словарь с именем в качестве ключа и суммой 
# премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии.
# premium = 0.1025

def create_list_rate():  # Создаем последовательность и помещаем в список
    print('С клавиатуры введите список элементов(ставки), по окончанию ввода нажмите Enter')
    new_list_rate = []
    while True:
        try:
            element = float(input('> '))
            float(element)
            new_list_rate.append(element)
        except:
            break
    return new_list_rate

def create_list_name():  # Создаем последовательность и помещаем в список
    print('С клавиатуры введите список элементов(имена), по окончанию ввода нажмите Enter')
    new_list_name = []
    while True:
        try:
            element = str(input('> '))
            if element == '' or element == ' ':
                break
            new_list_name.append(element)
        except:
            break
    return new_list_name

def create_list_dictionary_sum_premium(list_rate, list_name, premium=None):
    list_premium = []
    for i in range(len(list_rate)):
        list_premium.append(float("{0:.2f}".format(list_rate[i] * premium)))

    list_dict_premium = dict(zip(list_name, list_premium))
    return list_dict_premium

def main():
    new_list_rate = create_list_rate()
    # print(new_list_rate)
    new_list_name = create_list_name()
    # print(new_list_name)
    if (len(new_list_rate)) == 0 or (len(new_list_rate) == 0) \
            or len(new_list_rate) != len(new_list_name):
        print('Отсутствуют элементы в списке или кого-то не хватает')
        exit()
    list_dict_premium = create_list_dictionary_sum_premium(new_list_rate, new_list_name)
    print(list_dict_premium)

main()
###############  2 вариант  ####################
# def salary(names, rate, bonus):
#     workers ={}
#     for i in range (len(names)):
#         percent = float(bonus[i].replace('%',''))/100
#         workers[names[i]] = percent*rate[i] + rate[i]
#     return workers
# 
# names = ['Петров','Иванов','Денисов','Сидоров']
# rate = [15000, 12500, 13700, 21000]
# bonus = ['9.25%', '10.25%', '15%', '11.10%']
# workerSalary = salary(names, rate, bonus)
# print(workerSalary)