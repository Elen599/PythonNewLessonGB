# СПИСОК НЕЧЕТНЫХ ЭЛЕМЕНТОВ

#  Создайте вручную список с повторяющимися целыми числами.
#  Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
#  Нумерация начинается с единицы

def odd(x):
    if x == 0 : odd = True
    elif x % 2 == 0: odd = True
    else : odd = False
    return odd

myList = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 5, 5, 6, 6, 8, 8, 7, 2, 6, 1]
myNewList = []

for i in range(len(myList)):
    if not odd(myList[i]): myNewList.append(i+1)
print(myNewList)