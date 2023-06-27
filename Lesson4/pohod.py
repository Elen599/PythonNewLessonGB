import random

list_item = ['Палатка', 'Спальник', 'Пенка', 'Посуда', 'Фляга', 'Фонарик',
             'Горелка', 'Газ', 'Котелок', 'Топор', 'Нож', 'Тент',
             'Бахилы', 'Носки', 'Куртка', 'Штаны', 'Пуховка', 'Кофта',
             'Термобельё', 'Тапочки', 'Мыло', 'Спички', 'Трусы', 'Вода']

list_weight = [2.2, 2.1, 0.5, 1.2, 0.5, 0.5,
               0.5, 0.2, 1.5, 2.5, 0.6, 0.2,
               0.2, 0.1, 0.8, 0.7, 0.9, 0.6,
               0.3, 0.4, 0.1, 0.1, 0.1, 1.1]

max_capacity = 9

list_dictionary = dict(zip(list_item, list_weight))

def random_Bags_Of_Items(i):
    list_dictionary_random = random.sample(list_dictionary.keys(), len(list_dictionary))
    print('Вариант - ', i + 1)
    sum_weight = 0
    for j in range(len(list_dictionary)):
        if sum_weight + list_dictionary[list_dictionary_random[j]] <= max_capacity:
            sum_weight = sum_weight + list_dictionary[list_dictionary_random[j]]
            sum_weight = float('{:.1f}'.format(sum_weight))
            print(list_dictionary_random[j])
    print('')

def Main():
    print('Введите количество вариантов сборки рюкзака, \n которое хотели бы увидеть')
    num = int(input('>>> '))
    for i in range(num):
        random_Bags_Of_Items(i)

Main()
################ 2 вар
from itertools import combinations
#from itertools import permutations
myDict = {'продукты': 10, 'котел': 2.1, 'хлеб': 0.7, 'топор': 2.3, 'динамит': 1, 'вода': 1.5, 'палатка': 2, 'арбуз': 8}
maxWeight = 13
bigBag = {}

print("Вес всех вещей")
print(round(sum(myDict.values()),2))

weight = maxWeight
#    int(input("Введите грузоподъемность рюкзака в граммах\n"))

itemName = [*myDict.keys()]
variants = []
for n in range(1, len(itemName) + 1):
    comby = combinations(itemName, n)
#    print(list(comby))
    for variant in comby:
        sumItems = 0
        tempVariant = set()
        for el in variant:
            if sumItems + myDict[el] > weight:  # если сумма с добавление вещи превысит лимит, то
                continue
            sumItems += myDict[el]
            tempVariant.add(el)
        if tempVariant not in variants:  # полученное до этого множество добавляем в список вариантов (если его там еще нет)
            variants.append(tempVariant)

# проверим являются ли варианты подмножествами других вариантов, если да, то удалим эти варианты
i = 0
while i < len(variants):
    for j in range(0, len(variants)):
        if i == j:
            continue
        if variants[i] < variants[j]:
            variants.pop(i)
            break
    else:
        i += 1

print(f"Количество полученных вариантов: {len(variants)}")
print()

for var in sorted(variants, key=lambda x: sum(myDict[s] for s in x), reverse=True):
    print(*sorted(list(var)))
    wght = sum(myDict[s] for s in var)
    print(f" вес предметов {wght}")
    print()