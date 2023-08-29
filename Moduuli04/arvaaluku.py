import math
import random

randomLuku = random.randint(1, 10)
print(f' Debug randomLuku: {randomLuku}')

while True:
    vastaus = int(input("Yritä arvata random luku väliltä 1-10: "))
    
    
    try:
        print(vastaus)
        if randomLuku == vastaus:
            print(f'Oikein: \n Random luku {randomLuku} = vastaus {vastaus}')
            break
        elif vastaus < randomLuku:
            print('Liian pieni arvaus')
        elif vastaus > randomLuku:
            print('Liian suuri arvaus')
    except ValueError:
        print("Virheellinen syöte. Syötä kelvollinen luku.")

