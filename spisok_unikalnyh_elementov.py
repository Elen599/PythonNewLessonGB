# СПИСОК УНИКАЛЬНЫХ ЭЛЕМЕНТОВ

#  Вручную создайте список с целыми числами, которые повторяются. 
#  Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
#  *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.

# Способ 1 (длинное решение):

myList = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 5, 5, 6, 6, 8, 8, 7, 2, 6, 1]
print(myList)
myNewList = []

for i in myList:
    if i not in myNewList: myNewList.append(i)
print(myNewList)


# Способ 2 (короткое решение):

# myList = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 5, 5, 6, 6, 8, 8, 7, 2, 6, 1]
# myNewList2 = list(set(myList))               # Но тут используется множ-во
# print(myNewList2)