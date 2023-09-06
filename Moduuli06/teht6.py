import math

def pizza(cm, price):
    r = cm / 2
    area = math.pi * (r**2)
    unit_price = price / area
    return unit_price

input_halkaisija = int(input('Anna pizzan halkaisija senttimetreinä: '))
input_halkaisija2 = int(input('Anna toisen pizzan halkaisija senttimetreinä: '))

input_hinta = int(input('Anna pizzan hinta: '))
input_hinta2 = int(input('Anna tisen pizzan hinta: '))

pizza1 = pizza(input_halkaisija, input_hinta)
pizza2 = pizza(input_halkaisija2, input_hinta2)

if pizza1 < pizza2:
    print(f'Pizza 1 on edullisempi. Yksikköhinta = {pizza1}')
else: 
    print(f'Pizza 2 on edullisempi. Yksikköhinta = {pizza2}')


