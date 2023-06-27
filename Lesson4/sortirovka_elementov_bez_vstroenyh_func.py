# Сортировка элементов без встроенной функции
#
# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии


def superSort(myList):
    for i in range (len(myList)):
        for j in range(i, len(myList)):
            if i == j : continue
            elif myList[i] > myList[j] :
                myList[i], myList[j] = myList[j], myList[i]
    return myList
myList = [6, 3, 1, 2, 5, 7, 8, 2, 5, 2, 5, 7, 7, 9, 1, 0, 9, 1, 3, 4]
print(superSort(myList))