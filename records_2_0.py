scores = []
choice = None
while choice != 0:
    print('''
    Рекорды
    0 - Выйти
    1 - Показать рекорды
    2 - Добавить рекорд
    ''')
    choice = int(input('Ваш выбор: '))
    if choice == 0:
        print('До свидания!')
    elif choice == 1:
        print('Рекорды: ')
        print('ИМЯ\tРЕЗУЛЬТАТ')
        for entry in scores:
            score, name = entry
            print(name, '\t', score)
    elif choice == 2:
        name = input('Впишите имя игрока: ')
        score = int(input('Введите рекорд игрока: '))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
    else:
        print('Пункта', choice, 'нет в меню.')
input('Нажмите энтер чтобы выйти')
