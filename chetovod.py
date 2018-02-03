print('Привет! Я посчитаю по твоей просьбе ;)')
st = int(input('С какого числа начать считать? '))
fin = int(input('Каким числом закончить счет? '))
step = int(input('Какой должен быть шаг между числами? '))
for i in range(st, fin + 1, step):
    print(i, end=' ')
