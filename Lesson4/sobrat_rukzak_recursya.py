# Cобрать рюкзак через рекурсию

myDict = {'продукты': 10, 'котел': 2.1, 'хлеб': 0.7, 'топор': 2.3, 'динамит': 1, 'вода': 1.5, 'палатка': 2, 'арбуз': 8}
listKeys = list(myDict.keys())
listItems = list(myDict.values())
print(type(listItems))
maxWeight = 13
someList=[]
def func(someList, index, weight):
    print('Уже уложено:', someList)
    for i in range(index, len(listKeys)):
        print('Пробуем положить', listKeys[i])
        if listItems[i]+weight <= maxWeight :
            emptyList = someList.copy()
            emptyList.append(listKeys[i])
            print('Влазит')
            func(emptyList, i+1, weight+listItems[i])
        else: print('Не влазит')
    if len(someList) >= 3 : print(someList, weight)
func(someList, 0, 0)

arr_matrix = [[5, 4, 3],
              [2, 4, 6],
              [4, 7, 9],
              [8, 1, 6],
              [5, 2, 5],
              [3, 4, 2],
              [2, 5, 0]]

def print_matrix():
    for row in arr_matrix:
        print(row)
    print('')

def columns_matrix():
    count = 0
    for i in arr_matrix:
        count += len(i)
    if count / len(arr_matrix) == len(arr_matrix[0]):
        return len(arr_matrix[0])
    else:
        return 0

def transpose_matrix(len_row, len_col):
    transpose_matrix = []
    for j in range(len_col):
        list_temp = []
        for k in range(len_row):
            list_temp.append(0)
        transpose_matrix.append(list_temp)

    for a in range(len(arr_matrix)):
        for b in range(len(arr_matrix[0])):
            transpose_matrix[b][a] = arr_matrix[a][b]
    for row in transpose_matrix:
        print(row)

def main():
    len_row = len(arr_matrix)
    len_col = columns_matrix()
    print_matrix()
    transpose_matrix(len_row, len_col)

main()

