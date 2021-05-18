"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для
перевода: какой тип данных выбрать, в теле функции или снаружи.
"""


def num_translate(num, list):
    if list.get(num):
        return f'{list[num][0]} по-русски {list_num[num][1]}'
    else:
        return list.get(num)


list_num = {
    0: ['zero', 'ноль'],
    1: ['one', 'один'],
    2: ['two', 'два'],
    3: ['tree', 'три'],
    4: ['four', 'четыре'],
    5: ['five', 'пять'],
    6: ['six', 'шесть'],
    7: ['seven', 'семь'],
    8: ['eight', 'восемь'],
    9: ['nine', 'девять'],
    10: ['ten', 'десять']
}

while True:
    get_num = input('Введите число от 0 до 10 (для выхода: n) ')
    if get_num.isdigit():
        print(num_translate(int(get_num), list_num))
    elif get_num == 'n':
        break

"""
2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными, 
начинающимися с заглавной буквы. Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два"
"""


def num_translate_adv(num, list, numi):
    if list.get(num):
        if numi[0].isupper():
            return f'{list[num][0].capitalize()} по-русски {list_num[num][1].capitalize()}'
        else:
            return f'{list[num][0]} по-русски {list_num[num][1]}'
    else:
        return list.get(num)


e = 0

while True:
    get_num_n = input('Введите цифру по-английски от 0 до 10 (для выхода: n)  ')
    for i, val in enumerate(list_num):
        if get_num_n == 'n':
            e = 1
            break
        elif get_num_n.lower() == list_num[i][0]:
            print(num_translate_adv(i, list_num, get_num_n))
    if e == 1:
        break

"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, 
в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. 
Например:
>>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"], 
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?
"""


def thesaurus(name):
    list_names = {}
    for i, val in enumerate(name):
        if list_names.get(val[0]):
            list_names[val[0]].append(val)
        else:
            list_names[val[0]] = list(name[i].split())
    print(list_names)


thesaurus(['Мария', 'Светлана', 'Катерина', 'Любовь', 'Михаил', 'Сергей', 'Кирилл', 'Лариса'])

"""
4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате 
«Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные 
по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
>>> >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": "Петр Алексеев"
    }, 
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"], 
        "А": ["Анна Савельева"]
    }
}
"""


def thesaurus_adv(get_list):
    fam = {}
    for i, val in enumerate(get_list):
        split_name = list(str(val).split())
        if not fam.get(split_name[1][0]):
            fam[split_name[1][0]] = {}
        if not fam[split_name[1][0]].get(split_name[0][0]):
            fam[split_name[1][0]][split_name[0][0]] = []
        fam[split_name[1][0]][split_name[0][0]].append(str(get_list[i]))
    print(fam)


thesaurus_adv(['Станислав Сапожник', 'Игорь Бабичев', 'Мария Сергеева', 'Светлана Ковалева', 'Катерина Петрова',
               'Любовь Михайлова', 'Михаил Сергеев', 'Сергей Блинкен', 'Кирилл Ортынский', 'Лариса Потеевна',
               'Михаил Архангельский', 'Сергей Титов', 'Игорь Тараканов'])

