"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv
user_list =[
        {'name': 'Oleg', 'age': 96, 'job': 'Scientist'}, 
        {'name': 'Igor', 'age': 81, 'job': 'worker'}, 
        {'name': 'Stepan', 'age': 41, 'job': 'cleaner'},
        {'name': 'Viniamin', 'age': 25, 'job': 'policeman'},
    ]
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('joblist.csv', 'w', encoding = 'utf - 8') as job:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(job,fields,delimiter = ';')
        writer.writeheader()
        for user in user_list:
            writer.writerow(user)  

if __name__ == "__main__":
    main()
