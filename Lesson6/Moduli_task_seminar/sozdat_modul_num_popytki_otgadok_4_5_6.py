#  Задача 4. СОЗДАТЬ МОДУЛЬ (возвратить номер попытки отгадывания загадки)
# ✔ Создайте модуль с функцией внутри ("загадка").
# ✔ Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# ✔ Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

# Задача 5. ДОБАВИТЬ В МОДУЛЬ ФУНКЦИЮ (ХРАНИТ СЛОВАРЬ СПИСКОВ - "архив")
# ✔ Добавьте в модуль с загадками функцию, которая хранит словарь списков.
#    Ключ словаря - загадка, значение - список с отгадками.
# ✔ Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

# Задача 6. ФУНКЦИЯ ФОРМИРУЕТ  СЛОВАРЬ О РЕЗУЛЬТАТАХ ОТГАДЫВАНИЯ
# ✔ Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
#    Функция формирует словарь с информацией о результатах отгадывания.
#    Для хранения используйте защищённый словарь уровня модуля.
# ✔ Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
#    Для формирования результатов используйте генераторное выражение.

from import_modul_pod_psevdonimom_1 import rn

def zagadka(zag, otg, popit):
   print(zag)
   count = 1
   while count <= popit:
      otvet = input('Ваш ответ: ').lower()
      if otvet in otg:
         print(f'Угадали c {count} попытки')
         return count
      else:
         print('Попробуйте еще раз')
         count += 1
   print('Не угадали')
   return 0

# # Либо:
#
# myDict = {'Идет шуршит': ['шурашанчик'],
#                           'В кармане на П начинается': ['путылка'],
#                           'В кармене на Ы начинается': ['ышо одна путылка']}
# for i in myDict:
#     zagadka(i, myDict[i], 3)
#
# zagadka('Висит груша, нельзя скушать?', ['лампочка', 'лампа', 'лампомпулечка'], 3)



def archiv():
    myDict = {'Зимой и летом одним цветом': ['ель', 'елка', 'доллар'], 'Висит груша - нельзя скушать': ['груша', 'игрушка', 'лампочка']}

    for key, values in myDict.items():
        zagadka(key, values, rn.randint(1, 5))


_solutions = {}  # словарь protected (защищенный)
myDict = {'Зимой и летом одним цветом': ['ель', 'елка', 'доллар'], 'Висит груша - нельзя скушать': ['груша', 'игрушка', 'лампочка']}

def logAnswers(zag: str, popit: int):
    num = zag(zag, myDict[zag], popit)
    _solutions[zag] = [num, True if num else False]


def printDict():
    for k, v in _solutions.items():
        print(k, v)


if __name__ == '__main__':
    print(zagadka('Висит груша, нельзя скушать?', ['лампочка', 'лампа', 'лампомпулечка'], 3))