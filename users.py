print('заюш, введи логин и пароль, чтобы войти')
username = ''
while not username:
    username = input('Введите логин: ')
password = ''
while not password:
    password = input('Введите пароль: ')
if username == 'anton' and password == 'qwerty':
    print('заходи, любимый')
elif username == 'ksu' and password == '12345':
    print('свои без очереди')
elif username == 'guest' and password == 'guest':
    print('добро пожаловать, но только с гостевыми правами')
else:
    print('ты вообще кто?')
input('\nжмакни энтер, чтобы выйти')
