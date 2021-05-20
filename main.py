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


def thesaurus_adv(get_list):
    fam = {}
    for i, val in enumerate(get_list):
        split_name = list(str(val).split())
        if not fam.get(split_name[1][0]):
            fam[split_name[1][0]] = {}
        if not fam[split_name[1][0]].get(split_name[0][0]):
            fam[split_name[1][0]][split_name[0][0]] = []
        fam[split_name[1][0]][split_name[0][0]].append(str(get_list[i]))
    return fam


fam_list = thesaurus_adv(
    ['Станислав Сапожник', 'Игорь Бабичев', 'Мария Сергеева', 'Светлана Ковалева', 'Катерина Петрова',
     'Любовь Михайлова', 'Михаил Сергеев', 'Сергей Блинкен', 'Кирилл Ортынский', 'Лариса Потеевна',
     'Михаил Архангельский', 'Сергей Титов', 'Игорь Тараканов'])
print(fam_list)
fam_list_sort = {}
for i, val in (sorted(fam_list.items())):
    fam_list_sort[i] = val
print(fam_list_sort)

# Задача 5

"""
Импортирую библиотеку random для генерации случайных чисел
"""

import random


def get_jokes(n, w_1, w_2, w_3, n_r):
    """
    Создаю пустой список для формирования списка шуток
    Запускаю цикл на формирование запрошенного количества шуток
    Проверяю, если в списках слов есть индексы, то путем рандома записываю произвольное слова из списка в переменную
    по каждому списку отдельно, если индексов нет, значит слова в списках закончились и, чтобы не было ошибки, завершаю цикл
    Формирую текст из полученных слов
    Проверяю, если not_repeat = True (то есть вводился аргумент /), то удаляю выбранные слова из списка, чтобы они не повторялись
    Возвращаю полученный список с шутками
    """
    text = []
    for i in range(0, n):
        if len(w_1) != 0 and len(w_2) != 0 and len(w_3) != 0:
            ww_1 = w_1[random.randrange(0, len(w_1))]
            ww_2 = w_2[random.randrange(0, len(w_2))]
            ww_3 = w_3[random.randrange(0, len(w_3))]
            text_n = f'{ww_1} {ww_2} {ww_3}'
            text.append(text_n)
            if n_r == True:
                w_1.remove(ww_1)
                w_2.remove(ww_2)
                w_3.remove(ww_3)
        else:
            break
    return text


"""
Создаю списки со словами для шуток
"""
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

"""
Запрашиваю у пользователя количество требуемых шуток
проверяю, является ли введенное значение числом, если нет то прошу ввести еще раз
добавляю к введенному значени 'a' чтобы осуществить выход из поиска числа в строке, которая может иметь аргумент
проверяю, если в ответе есть  аргумент / то присваиваю not_repeat = True
формирую число введенное в начале перебором целочисленных символов, если нахожу не число, то заврешаю формирование количества шуток
передаю в функцию значения: число, содержание списков, значение no_repeat
"""

num = ''
not_repeat = False
while True:
    attempt = input('Введите количество шуток (если после цифры поставите / , то слова в шутках не будут повторяться ')
    if not attempt[0].isdigit():
        print('Введите сначала цифру, потом: / - если не хотите повторений')
    else:
        attempt = attempt + 'a'
        if attempt.find('/') > - 1:
            not_repeat = True
        for i in attempt:
            if i.isdigit():
                num = num + str(i)
            else:
                print(get_jokes(int(num), nouns, adverbs, adjectives, not_repeat))
                break
        break