# Напишите программу «Кто твой папа?», в которой пользователь будет вводить имя человека, а программа - называть отца этого человека.
family = {'Илья': 'Олег',
          'Иван': 'Людовик',
          'Игорь': 'Никита',
          'Ильяс': 'Рюрик'}  # сын - отец
choice = None
while choice != 0:
    print('''
        0 - выйти
        1 - найти отца
        2 - добавить родственников
        3 - изменить отцовство
        4- удалить запись
        ''')
    choice = int(input('Твой выбор: '))
    if choice == 0:
        print('Пока!')
    elif choice == 1:
        ans = input('О чьем отце хочешь узнать? ')
        if ans in family:
            relative = family[ans]
            print('У сына ', ans, ' отец ', relative)
        else:
            print('я не знаю такого :( ')
    elif choice == 2:
        ans = input('Чьего отца ты хочешь добавить? ')
        if ans not in family:
            relative = input('Какое описание у этой ошибки? ')
            family[ans] = relative
            print('Сын ', ans, ' и его отец добавлены в словарь.')
        else:
            print('Сын ', ans, ' уже есть в словаре.')
    elif choice == 3:
        ans = input('Чье отцовство хочешь переопределить? ')
        if ans in family:
            relative = input('Впиши имя отца: ')
            family[ans] = relative
            print('Отцовство ', ans, ' переопределено.')
        else:
            print('Такого сына нет, попробуй добавить в словарь.')
    elif choice == 4:
        ans = input('Какую запись хочешь удалить? ')
        if ans in family:
            del family[ans]
            print('Запись ', ans, ' удалена.')
        else:
            print('А её и нет. Фить ха. Везение.')
    else:
        print('Упс, что-то пошло не так( . В меню нет такого выбора. А у вас вообще нет выбора, по жизни.')
input('жмакни энтер, чтобы выйти')
