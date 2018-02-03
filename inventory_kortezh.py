inventory = ()
if not inventory:
    print('Вы безоружны')
input('press enter to continue')
inventory = ('меч-кладенец',
             'щит',
             'скатерть-самобранка',
             'русска_девица')
print('а теперь у вас есть', end=' ')
print(inventory)
for item in inventory:
    print(item)
input('press enter to continue')
print('Сейчас в вашем распоряжении ', len(inventory), ' предмета\ов')
input('press enter to continue')
if 'русска_девица' in inventory:
    print('Зря вы с собой бабу берете!')
index = int(input('Выберите номер предмета: '))
print('Под номером', index, 'в инвентаре находится', inventory[index])
low = int(input('Введите индекс начала среза: '))
high = int(input('Введите индекс конца среза: '))
print('Ваша выборка из инвентаря включает: ')
print(inventory[low: high])
input('press enter to continue')
sunduk = ('золото',
          'брыльянты')
print('Поздравляем, вы нашли сундук! В нем: ')
print(sunduk)
inventory += sunduk
print('Теперь у вас есть: ')
print(inventory)
input('press enter to exit')
