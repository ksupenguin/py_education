print('Привет! Здесь ты можешь найти расшифровку ошибок')
errors = {'203': 'Non-Authoritative Information',
          '400': 'Bad Request',
          '403': 'Forbidden',
          '404': 'Not Found'}
choice = None
while choice != 0:
    print('''
        0 - выйти
        1 - найти ошибку
        2 - добавить описание
        3 - изменить описание
        4- удалить
        ''')
    choice = int(input('Твой выбор: '))
    if choice == 0:
        print('Пока!')
    elif choice == 1:
        ans = input('О какой ошибке хочешь узнать? ')
        if ans in errors:
            explanation = errors[ans]
            print('Ошибка ', ans, ' означает ', explanation)
        else:
            print('я не знаю такой :( ')
    elif choice == 2:
        ans = input('Какую ошибку хочешь добавить? ')
        if ans not in errors:
            explanation = input('Какое описание у этой ошибки? ')
            errors[ans] = explanation
            print('Ошибка ', ans, ' добавлена в словарь.')
        else:
            print('Ошибка ', ans, ' уже есть в словаре.')
    elif choice == 3:
        ans = input('Какую ошибку хочешь переопределить? ')
        if ans in errors:
            explanation = input('Впиши описание ошибки: ')
            errors[ans] = explanation
            print('Ошибка ', ans, ' переопределена.')
        else:
            print('Такой ошибки нет, попробуй добавить в словарь.')
    elif choice == 4:
        ans = input('Какую ошибку хочешь удалить? ')
        if ans in errors:
            del errors[ans]
            print('Ошибка ', ans, ' удалена.')
        else:
            print('А её и нет. Фить ха. Везение.')
    else:
        print('Упс, что-то пошло не так( . В меню нет такого выбора. А у вас вообще нет выбора, по жизни.')
input('жмакни энтер, чтобы выйти')
