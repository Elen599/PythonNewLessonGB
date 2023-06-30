#  ТРАНСПОНИРОВАНИЕ МАТРИЦЫ

# ✔Напишите функцию для транспонирования матрицы

def transponse_matrix(*l_list: list[[int]]) -> list[()] | str:
    matrix_transparent: bool = True
    box = len(l_list[0])
    for i in list(l_list):
        if len(i) != box:
            matrix_transparent = False
    if matrix_transparent:
        return list(zip(*l_list))
    else:
        return "Матрицу нельзя транспонировать"


print(transponse_matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]))

####################  2 вариант  #######################
# START = 0
# def transponse_matrix(arr_mtr, s):
#     res_matrix = []
#     for j in range(len(arr_mtr[s])):
#         box = []
#         for i in range(len(arr_mtr)):
#             box.append(arr_mtr[i][j])
#         res_matrix.append(box)
#     return res_matrix
#
# arr_matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
# result_matrix = transponse_matrix(arr_matrix, START)
#
# for el in result_matrix:
#    print(*el)


################  вариант без функции  #########
# import numpy as np
# def transpons
# arr_matrix =  np.array([[1, 5, 9], [3, 5, 7]])
# arr_transponse = arr_matrix.transponse()
# print(arr_matrix)