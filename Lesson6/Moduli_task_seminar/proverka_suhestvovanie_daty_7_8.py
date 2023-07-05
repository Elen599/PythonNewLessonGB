# Задача 7. ПРОВЕРКА ДАТЫ (СУЩЕСТВУЕТ ЛИ ОНА)

# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

def calendar(date: str):
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        elif 1 <= day <= 28 + is_visokos_year(year):
            return True
        else:
            return False
    return False


def is_visokos_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

if __name__ == '__main__':
    print(calendar('12.12.2016'))
    print(calendar('29.02.2016'))

# Задача 8 (создана в файле: __init__.py)

# Создайте пакет с всеми модулями, которые вы создали за время занятия.
# Добавьте в __init__ пакета имена модулей внутри дандер __all__.
# В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.

# from sesozdat_modul_num_popytki_otgadok_4 import printDict, logAnswers, archiv
# from proverka_suhestvovanie_daty_7_8 import calendar, is_visokos_year
#
# __all__ = ["printDict", "logAnswers", "archiv"]
# __all__ = ["calendar", "is_visokos_year"]