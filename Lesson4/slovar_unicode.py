# Словарь юникод

# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.



def dictUnicode(numIn):
    numIn = list(map(int, numIn.split(' ')))
    maxN = max(numIn)
    minN = min(numIn)
    for i in range(minN, maxN + 1):
        myDict[chr(i)] = i
    return myDict
numIn = input('вводим два числа через пробел')
myDict = {}

print(dictUnicode(numIn))