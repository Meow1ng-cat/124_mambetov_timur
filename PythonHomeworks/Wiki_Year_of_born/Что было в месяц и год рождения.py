import requests
import time


def season_events(month, year):
    file = open(month+'('+str(year)+').txt', 'w')
    file.write('Вы родились в месяце '+month+' в '+str(year) +
               ' году. Вот список событий произошедших в год вашего рождения: \n')
    wiki_page = requests.get('https://ru.wikipedia.org/wiki/Категория:' + month + '_' + str(year) + '_года').text
    start_point = wiki_page.find('<p>Показан')
    fact_count = str()
    for i in range(start_point + 12, wiki_page.find('стран', start_point) - 1):
        fact_count += wiki_page[i]
    fact_count = int(fact_count)
    for i in range(0, fact_count + 1):
        href_find = wiki_page.find('<a href="/wiki/', start_point)
        fact_start_find = wiki_page.find('title="', href_find)
        fact_end_find = wiki_page.find('">', fact_start_find)
        start_point = fact_start_find
        if i > 0:
            fact = str()
            for j in range(fact_start_find + 7, fact_end_find):
                fact += wiki_page[j]
            fact += "\n"
            try:
                file.write(fact)
            except UnicodeEncodeError:
                file.write('!Событие содержит недопустимый символ. Оно будет пропущено.!\n')
    file.close()


Months_of_year = \
    ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')

while 'Month' not in globals():
    try:
        Month = input('Введите месяц вашего рождения: ')
        if Month not in Months_of_year:
            print('Вы ввели некоретное значение. Введите одно значение из списка: ', Months_of_year)
            del Month
    except ValueError:
        print('Вы ввеили некоректное значение')
while 'Year' not in globals():
    try:
        Year = int(input('Введите год вашего рождения: '))
        if (Year < 1933) or (Year > time.localtime(time.time())[0]):
            print('Введите значение в диапозоне от 1933 до', time.localtime(time.time())[0])
            del Year
    except ValueError:
        print('Вы ввеили некоректное значение.')

season_events(Month, Year)
