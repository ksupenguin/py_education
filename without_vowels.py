message = input('Введите текст: ')
VOWELS = 'уеэоаыяию'
new_mess = ''
for letter in message:
    if letter.lower() not in VOWELS:
        new_mess += letter
print('А вот ваш текст без гласных: ' + new_mess)
