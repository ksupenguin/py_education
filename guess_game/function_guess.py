def game(low, high):
    print('Приветствую тебя в нашей игре!')
    print('Суть игры: ты загадываешь число от ', low, 'до ', high, ', а компьютер должен отгадать.')
    q = input('Ты готов?')
    while q == 'нет':
        print('Ну ладно. Ну а теперь?')
        q = input('Ты готов?')
    print('Отлично! Загадай число от ', low, 'до ', high, ', и не говори его мне ;)')
    resp = ''
    num = high - (high - low) // 2
    resp = input('Это число' + str(num) + '?')
    while resp != 'да':
        dif = input('Ваше число больше или меньше моего?')
        if dif == 'больше':
            num = num + (high - num) // 2
        else:
            num = num - (high - num) // 2
        resp = input('Это число' + str(num) + '?')
    print('Ура! Я отгадал!')
    input('нажми энтер, чтобы выйти')
