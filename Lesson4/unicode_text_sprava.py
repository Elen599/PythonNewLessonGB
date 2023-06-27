# Юникод текста справа
#
# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

def textPrinting(text, count, lenMaxWord):
    print(count, text.rjust(lenMaxWord, '-'))
def superFunc(text):
    text = "".join([i for i in text.lower() if i.isalpha() or i == " "])
    myWords = sorted(text.split(' '))
    count = 1
    lenMaxWord = len(max(myWords, key=len))  # Длина макс. слова. Чтобы не поплыл текст при выводе
    for i in myWords:
        textPrinting(i, count, lenMaxWord)
        count += 1

text = 'пивная, еще парочку..., Эй ты, дай папироску, у тебя штаны в полоску'
superFunc(text)