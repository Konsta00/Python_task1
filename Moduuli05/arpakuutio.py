import random

dice_count = int(input('Anna arpakuutioiden lukumäärä: '))
sum = 0

for i in range(dice_count):
    randomThrow = random.randint(1, 6)
    print(f'Heitto nro {i+1} | {randomThrow}')
    sum += randomThrow

print(sum)