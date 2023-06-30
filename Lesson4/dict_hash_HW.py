#  ВОЗВРАЩЕНИЕ СЛОВАРЯ С ХЕШЕМ

#  Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
#  где ключ — значение переданного аргумента, а значение — имя аргумента.
#  Если ключ не хешируем, используйте его строковое представление.

def hash_dicts(**kwargs):
    res = dict()
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set)):
             value = str(value)
        res[value] = key
    return res

print(hash_dicts(a = 5, b = [5, 6], галка = {'птица'}))

#########################################################
# def dict_hash(**kwargs):
#     res = {}
#     for key, el in kwargs.items():
#         if el.__hash__ == None:
#             el = str(el)
#         res[el] = key
#     return res
#
# print(dict_hash(a = 5, b = [5, 6]))