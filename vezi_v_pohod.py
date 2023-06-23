# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите, какие вещи влезут в рюкзак, передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

things = {'спички': 20, 'компас': 100, 'консервы': 500, 'футболка': 300,
          'термос': 1000, 'аптечка': 200, 'куртка': 600, 'бинокль': 400, 'удочка': 1200,
          'салфетки': 40, 'бутерброды': 820, 'палатка': 5500, 'спальный мешок': 2250, 'нож': 10}
ves = int(input('Введите максимальную грузоподъёмность рюкзака(в кг): '))
temp_w = 0
temp_things = []
sorted_things = dict(sorted(things.items(), key=lambda x: -x[1]))

for k, v in sorted_things.items():
    if temp_w + v <= ves:
        temp_w = temp_w + v
        temp_things.append(k)

print(f"В рюкзак войдут вещи: {temp_things}")