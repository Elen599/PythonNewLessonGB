# СЛОВАРЬ СПИСКА ИЗ КОРТЕЖА

#  Создайте вручную кортеж содержащий элементы разных типов.
#  Получите из него словарь списков, где: ключ — тип элемента,
#  значение — список элементов данного типа.

myTuple = (1, 2.3, 'hi', True, 'Hello', 5)
myDict = {}
myList = list(myTuple)

for i in myList:
    if type(i) in myDict.keys() : myDict[type(i)].append(i)
    else:
        myValue = []
        myValue.append(i)
        myDict[type(i)] = myValue
print(myDict)       #Можно так вывести

for key in myDict:
    print(f"type: {key}  value: {myDict[key]} ")      # а можно перебрать попарно