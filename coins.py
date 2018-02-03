import random

number = 0  # число бросков
orel = 0
reshka = 0
while number < 100:
    number += 1
    side = random.randint(1, 2)  # 1 орел 2 решка
    if side == 1:
        orel += 1
    else:
        reshka += 1
print(orel, 'раз выпал орел')
print(reshka, 'раз выпала решка')
