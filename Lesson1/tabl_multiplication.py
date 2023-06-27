print('Таблица умножения')

for i in range(2, 10):
    for k in range(2, 6):
        print(f'{k} * {i} = {i * k}\t', end='')
    print('')
print('')
for i in range(2, 10):
    for k in range(6, 10):
        print(f'{k} * {i} = {i * k}\t', end='')
    print('')