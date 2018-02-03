def validation():
    low = int(input('Введите первое число: '))
    high = int(input('Введите второе число: '))
    while high < low:
        print('Первое число должно быть меньше второго.')
        low = int(input('Введите первое число: '))
        high = int(input('Введите второе число: '))
    return low, high
