# Юникод символ по убыванию
#
# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.


def textUnicode(text):
    uniList = []
    text = list(text)
    text.sort(reverse = True)
    print(text)
    for i in text :
        uniList.append(ord(i))
    return uniList

text = 'пивная, еще парочку..., Эй ты, дай папироску, у тебя штаны в полоску'
print(text)
text = "".join([i for i in text.lower() if i.isalpha() or i ==" "]).replace(' ','')
print(set(textUnicode(text)))
################  2 вариант  #############

def create_list():    # Создаем последовательность и помещаем в список
    print('С клавиатуры введите список элементов(числа), по окончанию ввода нажмите Enter')
    new_list = []
    while True:
        try:
            element = int(input('> '))
            int(element)
            new_list.append(element)
        except:
            break
    return new_list

def sort_bubble(sort_list):     # Сортируем по возрастанию
    for i in range(0, len(sort_list)):
        for j in range(0, len(sort_list) - i - 1):
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
    return sort_list

def main():
    new_list = create_list()
    print(new_list)
    if len(new_list) == 0:
        print('Отсутствуют числовые элементы в списке')
        exit()
    sort_list = sort_bubble(new_list)
    print(sort_list)

main()