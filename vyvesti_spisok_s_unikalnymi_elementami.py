#  Дан список повторяющихся элементов.
#   ✔ Вернуть список с дублирующимися элементами.
#   ✔ В результирующем списке не должно быть дубликатов.

##############  1 вариант ####################  # count()
my_list = [100, 72, 33, 72, 54, 33, 55, 100, 100, 72, 2, 8, 3, 5, 33]
res_list = []
for i in my_list:
    if i not in res_list:
        if my_list.count(i) > 1:
            res_list.append(int(i))
print(my_list, f"Список с дублирующимися элементами: {res_list}", sep='\n')

################ 2 вариант ####################  # append()
# from random import randint
# RND_N = 20
#
# my_list = []
# ar_res = []
# for _ in range(RND_N):
#     my_list.append(randint(1, 5))
# print(*my_list)
#
# for el in my_list:
#     if el not in ar_res:
#         ar_res.append(el)
# print(f"Список с дублирующимися элементами: {ar_res}")

################  3  вариант  ###################  # set()
# my_list = [1, 2, 3, 2, 4, 3, 5]           # если цифра повторяется только 2 раза
# unique_set = set()
# res_list = []
# for el in my_list:
#     if el in unique_set:
#         res_list.append(el)
#     else:
#         unique_set.add(el)
# print(my_list, f"Список с дублирующимися элементами: {res_list}", sep='\n')