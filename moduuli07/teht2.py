nimet = set()
input_name = input('[Tyhjä merkkijono lopettaa ohjelman] \nSyötä nimi: ')

while True:
    if input_name == '':
        break

    if input_name not in nimet:
        nimet.add(input_name)
        print(f'Uusi nimi {input_name} lisätty')
        input_name = input('Lisää uusi nimi: ')
        print(nimet)
    elif input_name in nimet:
        print('Aiemmin syötetty nimi')
        input_name = input('Syötä nimi uudestaan: ')

for i, n in enumerate(nimet):
    print(f'{i+1}). {n}')