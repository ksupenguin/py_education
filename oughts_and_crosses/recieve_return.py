def display(message):
    print(message)


def give_me_five():
    five = 5
    return five


def ask_yes_no(question):
    """задает вопрос с ответом да или нет"""
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


# основная часть
display('Вам сообщение: \n')
number = give_me_five()
print('Вот что возвратила функция гив_ми_файв: ', number)
answer = ask_yes_no('\n Пожалуйста, введите y или n: ')
print('Спасибо, что ввели', answer)
input('press enter to exit')
