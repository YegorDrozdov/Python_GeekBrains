'''1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.'''

with open('result_1.txt', 'w', encoding='UTF-8') as res:
    while True:
        x = input('Пишите сюда все что угодно ')
        if x:
            print(x, file=res)
        else:
            break

'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.'''
x = 0
with open('result_1.txt', 'r') as rd:
    for i, line in enumerate(rd):
        x += line.count('\n')
        print(f'Колличество слов в {i + 1} строке - {len(line.split())}')
print(f'Колличество строк в файле {x}')

'''3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.'''

s = 0
total_salary = 0
with open('office.txt', 'r', encoding='utf-8') as f:
    print(f"Сотрудники имееющие оклад менее 20 тыс: ")
    for line in f:
        k = line.split()
        if line != '\n':
            total_salary += int(k[-2])
            if int(k[-2]) < 20000:
                print(f"   {' '.join(k[:2])}")
            s += line.count('\n')
print(f'Среднея величина дохода сотрудников - {total_salary / s}')

'''4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.'''

from googletrans import Translator

# from goslate import Goslate
translator = Translator()
# gs = Goslate()
with open('eng_numbers.txt', 'r', encoding='utf-8') as eng, open('ru_numbers.txt', 'w', encoding='utf-8') as ru:
    for ln in eng:
        line_k = ln.split()
        line_k[0] = translator.translate(line_k[0], dest='ru').text.capitalize()
        # line_k[0] = gs.translate(ln.split()[0], 'ru').capitalize()
        res = ' '.join(line_k)
        print(res, file=ru)

'''5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''
from random import random, randint

total = 0
with open('digits_file.txt', 'w', encoding='utf-8') as dg:
    while -10000 < total < 10000:
        x = randint(-100, 100)
        print(x, end=' ', file=dg)
        total += x
        print(f'Cумма чисел в файле {total}')

'''6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}'''

from re import findall

lessons = {}
with open('tutorials.txt', 'r', encoding='utf-8') as tut:
    for line in tut:
        lessons.setdefault(line.split()[0], sum(
            map(int, findall(r'\d+', line))))  # key = line.split()[0], value = sum(map(int, findall(r'(\d+)', line)))
print(lessons)

'''7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.'''
from re import findall
from json import dump

lst, dct, dct_average, average, counter = [], {}, {}, 0, 0
with open('firms.txt', 'r', encoding='utf-8') as fm:
    for firm in fm:
        x = firm.split()[0]
        y1, y2 = map(int, findall(r'\d+[\d]', firm))
        dct.setdefault(x, y1 - y2)

lst.append(dct)
for value in lst[0].values():
    if value > 0:
        average += value
        counter += 1
dct_average.setdefault("average_profit", average / counter)
lst.append(dct_average)

with open('my_file.json', 'w', encoding='utf-8') as js:
    dump(lst, js)
