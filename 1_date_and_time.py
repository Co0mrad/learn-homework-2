"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date,timedelta,datetime


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
dt_now = datetime.now()
print(dt_now.strftime('%d.%m.%Y'))

yest_delta = timedelta(days = 1)
yest_day = dt_now - yest_delta
print(yest_day.strftime('%d.%m.%Y'))

delta_day = timedelta(days = 30)
over_delta = dt_now - delta_day
print(over_delta.strftime('%d.%m.%Y'))



def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
str_date = "01/01/20 12:10:03.234567"
date_str = datetime.strptime(str_date, '%d/%m/%y %H:%M:%S.%f')
print(date_str)

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
