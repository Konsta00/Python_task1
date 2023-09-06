
input_gallon = int(input('Anna gallona määrä mikä muutetaan litroiksi: '))

def gallonToLiter(gallon):
    return gallon * 3.785

while True:

    if input_gallon < 0:
        print('Negatiivinen määrä!')
        break
    elif input_gallon > 0:
        print(f'Määrä litroina: {gallonToLiter(input_gallon)}')
        input_gallon = int(input('Anna gallona määrä: '))
    else:
        input_gallon = int(input('Väärä syöte! \n Anna gallona määrä: '))




