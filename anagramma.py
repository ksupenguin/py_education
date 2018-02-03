import random

WORDS = ('рандом',
         'картошка',
         'апельсин',
         'декабрист',
         'любовь')
word = random.choice(WORDS)
correct = word
anagr = ''
while word:
    position = random.randrange(len(word))
    anagr += word[position]
    word = word[: position] + word[position + 1:]
print('Добро пожаловать в игру Анаграммы!')
print('Твоя задача - переставить буквы так, чтобы получилось осмысленное слово')
print('Для выхода нажмите энтер без ввода своей версии')
print('\nВот анаграмма: ', anagr)
guess = input('Попробуйте отгадать слово: ')
while guess != correct and guess != '':
    print('К сожалению, это неверно. Попробуйте еще раз.')
    guess = input('Попробуйте отгадать слово: ')
if guess == correct:
    print('Да, вы отгадали! Поздравляю!')
input('нажмите энтер, чтобы выйти')
