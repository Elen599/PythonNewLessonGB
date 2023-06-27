# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

# data = open(r"text.txt", "r", encoding="UTF-8")
# text = data.read()
# data.close()
# delete = '.,!?;:-[]{}()='
# newText = [i.rstrip(delete).lower() for i in text.split() if len(i.rstrip(delete)) > 1]
# print(*sorted(set(newText), key=newText.count, reverse=True)[:10], sep='\n')

################  2  вариант  ###################
STEP = 1
TOP = 9
count = 0
user_str = input('Введите текст: ')
ar_str = user_str.lower().replace('-',' ')\
    .replace(',',' ').replace(':',' ')\
    .replace('.',' ').replace('!',' ').replace('?',' ').replace('  ',' ').split()
str_dict = {}

for el in ar_str:
    if el in str_dict:
        str_dict[el] += STEP
    else:
        str_dict[el] = STEP

str_dict = dict(sorted(str_dict.items(), reverse=True, key=lambda x: x[1]))

for key, el in str_dict.items():
    print(str(key), '-', str(el))
    count += STEP
    if count > TOP: break