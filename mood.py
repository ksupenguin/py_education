import random

print('Сейчас я угадаю твоё настроение. тааак, секундочку...')
mood = random.randint(1, 3)
if mood == 1:
    print('Ага, у тебя хорошее настроение! Ну-ка делись :)')
elif mood == 2:
    print('Что-то непонятное.. Что-то ты молодец и не весел, и не грустен. Давай в сторону весел двигаться?)')
else:
    print('Ээй, не грусти! Тебя любят <3')
