import random

tahkot = int(input('Anna tahkojen maksimi määrä: '))

def throw_dice(tahko):
    return random.randint(1, tahko)

while True:

    num = throw_dice(tahkot)
    print(f'Heitetty luku: {num}')

    if num == tahkot:
        print('Osuma')
        break

