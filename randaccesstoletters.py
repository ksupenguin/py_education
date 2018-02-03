import random

word = input('Введите слово: ')
high = len(word)
low = -len(word)
for i in range(len(word)):
    position = random.randrange(low, high)
    print('word.[' + str(position) + ']\t', word[position])
