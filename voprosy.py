name = input('Привет! Как тебя зовут? ')
sname = input(name + ', а отчество? ')
print('Какое красивое имя! ', name, sname, '!')
age = input(name + ', а сколько тебе лет? ')
while not age.isdigit():
    print('Ты ошибся. Попробуй снова.')
    age = input(name + ', а сколько тебе лет? ')
print(age, '?! Ничего себе! Совсем большой человек ;)')
sage = input('А сколько твоей второй половинке лет? ')
while not sage.isdigit():
    print('Ты ошибся. Попробуй снова.')
    sage = input('А сколько твоей второй половинке лет? ')
if age == sage:
    print('Да вы ровесники!')
else:
    print('То есть у вас разница в ', abs(int(age) - int(sage)), 'лет. Неплохо)')
