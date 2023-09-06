import random

def throw_dice():
    return random.randint(1, 6)

while True:

    num = throw_dice()
    print(f'Heitetty luku: {num}')

    if num == 6:
        break


