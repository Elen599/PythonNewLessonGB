#  ПРЕОБРАЗОВАНИЕ ДАННЫХ

#  Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
#  Целое положительное число, вещественное положительное или отрицательное число
#  Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
#  Строку в нижнем регистре в остальных случаях
 
sentence = (input('Введите данные (число)->  '))
if sentence.isdecimal() : print(int(sentence))
elif sentence[0] in '-0123456789' and sentence.count('.') in range(0,2) and sentence[1:].replace('.','').isdecimal():
     print(float(sentence))
elif sentence.isupper() : print(sentence.isupper())
else: print(sentence.islower())