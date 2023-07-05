# Задача 8

# Создайте пакет с всеми модулями, которые вы создали за время занятия.
# Добавьте в __init__ пакета имена модулей внутри дандер __all__.
# В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.

from sozdat_modul_num_popytki_otgadok_4_5_6 import printDict, logAnswers, archiv
from proverka_suhestvovanie_daty_7_8 import calendar, is_visokos_year

__all__ = ["printDict", "logAnswers", "archiv"]
__all__ = ["calendar", "is_visokos_year"]