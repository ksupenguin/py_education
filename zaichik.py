word = 'zaichik'
print('''
Памятка
0   1   2   3   4   5   6   7
------------------------------
  z   a   i   c   h   i   k
------------------------------
-7 -6  -5  -4  -3  -2  -1
''')
print('Введите начальный и конечный индексы для того среза зайчика, который хотите получить')
print('Для выхода нажмите энтер, не вводя начальную позицию')
start = None
while start != '':
    start = input('Введите начальный индекс: ')
    if start:
        start = int(start)
        finish = int(input('Введите конечный индекс: '))
        print('Срез выглядит как ')
        print(word[start:finish])
input('нажмите энтер, чтобы выйти')