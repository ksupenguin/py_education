a = int(input('Введите первое число'))
b = int(input('Введите второе число'))
while b == 0: b = int(input('Введите второе число'))
c = input('Что нужно сделать? (1- +, 2- -, 3- *, 4- /)').strip()
if (c == '1'):
    d = a + b
elif (c == '2'):
    d = a - b
elif (c == '3'):
    d = a * b
else:
    d = a / b
print(d)
