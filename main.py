# Задача 1


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


# Задача 2


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


# Задача 3


def thesaurus(*args):
    name =list(args)
    list_names = {}
    for i, val in enumerate(name):
        if list_names.get(val[0]):
            list_names[val[0]].append(val)
        else:
            list_names[val[0]] = list(name[i].split())
    print(list_names)


thesaurus('Мария', 'Светлана', 'Катерина', 'Любовь', 'Михаил', 'Сергей', 'Кирилл', 'Лариса')


# Задача 4


def thesaurus_adv(*args):
    fam = {}
    for i, val in enumerate(args):
        split_name = list(str(val).split())
        fam.setdefault(split_name[1][0],{})
        fam[split_name[1][0]].setdefault(split_name[0][0], [])
        fam[split_name[1][0]][split_name[0][0]].append(str(args[i]))
    return fam


fam_list = thesaurus_adv(
    'Станислав Сапожник', 'Игорь Бабичев', 'Мария Сергеева', 'Светлана Ковалева', 'Катерина Петрова',
     'Любовь Михайлова', 'Михаил Сергеев', 'Сергей Блинкен', 'Кирилл Ортынский', 'Лариса Потеевна',
     'Михаил Архангельский', 'Сергей Титов', 'Игорь Тараканов')
print(fam_list)
fam_list_sort = {}
for i, val in (sorted(fam_list.items())):
    fam_list_sort[i] = val
print(fam_list_sort)

# Задача 5

import random
from random import choice


def get_jokes(n, w_1, w_2, w_3, n_r):
    text = []
    for i in range(0, n):
        if len(w_1) != 0 and len(w_2) != 0 and len(w_3) != 0:
            text_n = f'{choice(w_1)} {choice(w_2)} {choice(w_3)}'
            text.append(text_n)
            if n_r.find('/'):
                w_1.remove(text_n.split(' ')[0])
                w_2.remove(text_n.split(' ')[1])
                w_3.remove(text_n.split(' ')[2])
        else:
            break
    return text


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

num = ''

while True:
    attempt = input('Введите количество шуток (если после цифры поставите / , то слова в шутках не будут повторяться) ')
    if not attempt[0].isdigit():
        print('Введите сначала цифру, потом: / - если не хотите повторений')
    else:
        attempt = attempt + 'a'
        for i in attempt:
            if i.isdigit():
                num = num + str(i)
            else:
                print(get_jokes(int(num), nouns, adverbs, adjectives, attempt))
                break
        break
#help(get_jokes)