# игра виселица: попробуй не умри
import random

HANGMAN = ('''
            -------
            |     |
            |     |
            |
            |
            |
            |
            |
            |______
            ''',
           '''
            -------
            |     |
            |     |
            |     0
            |
            |
            |
            |
            |______
           ''',
           '''
            -------
            |     |
            |     |
            |     0
            |    / \
            |
            |
            |
            |______
           ''',
           '''
            -------
            |     |
            |     |
            |     0
            |    /|\
            |     |
            |
            |
            |______
           ''',
           '''
            -------
            |     |
            |     |
            |     0
            |    /|\
            |     |
            |    / \
            |
            |______
           ''',
           '''
            -------
            |     |
            |
            |
            |
            |      0
            |     \\/
            |   \//\/\/
            |________
           ''')
MAX_MISTAKES = len(HANGMAN) - 1
WORDS = ('рандом',
         'картошка',
         'апельсин',
         'декабрист',
         'любовь')
word = random.choice(WORDS)
so_far = '_' * len(word)
wrong = 0
used = []
print('Добро пожаловать в игру "Виселица"!')
while wrong < MAX_MISTAKES and so_far != word:
    print(HANGMAN[wrong])
    print('Ты уже предлагал эти буквы: \n', used)
    print('Слово сейчас выглядит так:\n', so_far)
    guess = input('Введи букву: ')
    guess = guess.lower()
    while guess in used:
        print('Вы уже предлагали букву ', guess)
        guess = input('Введи букву: ')
        guess = guess.lower()
    used.append(guess)
    if guess in word:
        print('Да! Буква ', guess, 'есть в этом слове.')
        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print('К сожалению этой буквы нет в слове.')
        wrong += 1
if wrong == MAX_MISTAKES:
    print(HANGMAN[wrong])
    print('Упс! Кажется тебя повесили.')
else:
    print('Ты отгадал!')
print('Было загадано слово ', word)
input('жмакни энтер чтобы выйти')
