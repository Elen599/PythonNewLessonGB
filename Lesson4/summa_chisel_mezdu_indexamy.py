# Сумма чисел между тндексами
#
# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

def create_list():  # Создаем последовательность и помещаем в список
    print('С клавиатуры введите список элементов(ставки), по окончанию ввода нажмите Enter')
    new_list = []
    while True:
        try:
            element = int(input('> '))
            int(element)
            new_list.append(element)
        except:
            break
    return new_list

def sequence_sum(new_list, index_list):
    list_sum = []
    list_sum_min = []
    list_sum_max = []
    for item in new_list:
        if item >= index_list[0] and item <= index_list[1]:
            list_sum.append(item)
        elif item < index_list[0]:
            list_sum_min.append(item)
        elif item > index_list[1]:
            list_sum_max.append(item)
    if len(list_sum) != 0:
        return sum(list_sum)
    elif len(list_sum_min) != 0:
        return sum(list_sum_min)
    elif len(list_sum_max) != 0:
        return sum(list_sum_max)

def main():
    new_list = create_list()
    print(new_list)
    new_list.sort()
    print(new_list)
    index = str(input('Введите два индекса через пробел >>> '))
    index_list = index.split()
    index_list = [int(item) for item in index_list]
    index_list.sort()
    print(index_list)
    if (len(new_list)) == 0 or len(index_list) != 2:
        print('Отсутствуют элементы в списке или индексов не два')
        exit()
    print('Сумма = ', sequence_sum(new_list, index_list))

main()

############# 2 вариант  #########
# def indRange(ind, limit):
#     if ind < 0 : ind = 0
#     if ind > limit : ind = limit - 1
#     return ind
# def sumNums(myList, ind, ind2):
#     ind = indRange(ind, len(myList))
#     ind2 = indRange(ind2, len(myList))
#     sum = 0
#     for i in  range(ind, ind2+1):   #сумма включая числа под заданными инксами
#     #for i in range(ind+1, ind2):    # сумма без чисел под индексами
#         sum = sum + myList[i]
#     return sum
# myList = [1, 3, 5, 2, 4, 6, 8]
# ind = int(input('введите индекс №1 - >> '))
# ind2 = int(input('введите индекс №2 - >> '))
# print(sumNums(myList, ind, ind2))

###################  3 вариант  ####################
# def dictUnicode(numIn):
#     numIn = list(map(int, numIn.split(' ')))
#     maxN = max(numIn)
#     minN = min(numIn)
#     for i in range(minN, maxN + 1):
#         myDict[chr(i)] = i
#     return myDict
# numIn = input('вводим два числа через пробел')
# myDict = {}
#
# print(dictUnicode(numIn))