# Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его опадать. Компьютер сообщает игроку, сколько букв в слове, и дает пяtь попыток узнаtь, есtь ли какая-либо буква в слове
import random

WORDS = ('рандом',
         'картошка',
         'апельсин',
         'декабрист',
         'любовь')
word = random.choice(WORDS)
correct = word
length = len(word)
print('Привет! Я загадал слово, твоя задача - его отгадать. В моем слове ', length, ' букв.')
print('У тебя есть пять попыток, чтобы проверить, есть в слове определенная буква.')
input('нажми энтер для продолжения')
count = 1
while count < 6:
    count += 1
    let = input('Какую букву будем проверять? ')
    if let in word:
        print('Есть такая буква в этом слове!')
    else:
        print('В моем слове нет такой буквы')
guess = input('Итак, твоя версия? ')
if guess == correct:
    print('Ура! Ты прав! Поздравляю!')
else:
    print('К сожалению, ты проиграл(')
input('нажми энтер для выхода')
