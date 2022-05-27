"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""
import re
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
with open('referat.txt', 'r', encoding ='utf -8') as referat:
    text = referat.read()#прочитали файл в переменную 
    text_len = len(text)#подсчитали длину строки
    words = len(text.split()) #подсчитали колличество слов в тексте
    with open('referat2.txt', 'w', encoding ='utf -8') as referat2:
        for dote in text:
            dote = text.replace('.','!')
        referat2.write(f'{dote}\nДлина переменной в которой лежит текст:{text_len}\nКолличество слов в тексте:{words} ')   
    
    

if __name__ == "__main__":
    main()
