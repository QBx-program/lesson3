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
        print(f'{list[num][0]} по-русски {list_num[num][1]}')
    else:
        print(list.get(num))

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
        num_translate(int(get_num),list_num)
    elif get_num == 'n':
        break

