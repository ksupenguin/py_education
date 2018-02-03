errors = {'203': 'Non-Authoritative Information',
          '400': 'Bad Request',
          '403': 'Forbidden',
          '404': 'Not Found'}
errors.keys()
print(errors.keys())  # возвращает все ключи
print(errors.get('123', 'eeerrrrrooooorrr'))  # возвращает значение по ключу, если нет , то дефолтное
print(errors.values())  # возвращает все значения
print(errors.items())  # возвращает значения всех пар
