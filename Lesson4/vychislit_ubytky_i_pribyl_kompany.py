# Вычислить убытки и прибыль компании

# Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
list_company = ['New Company', 'Real Company', 'Company', 'CompBiz',
                'Mega brand', 'Mega King', 'Everything', 'Modest']

list_profit_and_loss = [(100, 200, 300, -100, -200), (200, 600, 400, -300, -400),
                        (200, 300, 300, -500, -100), (200, 200, 100, -100, -400),
                        (100, 100, 100, -100, -100), (100, 300, 100, -100, -100),
                        (300, 200, 100, -100, -200), (400, 600, 100, -100, -100)]

list_dictionary = dict(zip(list_company, list_profit_and_loss))
keys = list(list_dictionary.keys())

def check_company():
    for i in range(len(list_dictionary)):
        if sum(list_dictionary[keys[i]]) < 0:
            return False
    return True

print(check_company())
############ 2 вар  ##########
# def positiveBalans(company):
#     for comp, balans in company.items():
#         if sum(balans) >= 0:
#             x = True
#         else:
#             x = False
#             break
#     return True if x == True else False
# 
# company = {
#     'CompanyOne': [1000, 123331, 1000, 2000],
#     'CompanyTwo': [9999, -1000, 12000],
#     'CompanyThree': [10000, -23322, 100000, -9999]
# }
# print(positiveBalans(company))