import math

kl1 = input('Syötä kokonaisluku:')
try: 
    value = int(kl1)
except ValueError:
    kl1 = input('Valitse kokonaisluku:')

kl2 = input('Syötä toinen kokonaisluku:')
try: 
    value = int(kl2)
except ValueError:
    kl2 = input('Valitse kokonaisluku:')

kl3 = input('Syötä vielä yksi kokonaisluku:')
try: 
    value = int(kl3)
except ValueError:
    kl3 = input('Valitse kokonaisluku:')

summa = int(kl1) + int(kl2) + int(kl3)
tulo = int(kl1)*int(kl2)*int(kl3)
keskiarvo = int(summa / 3)

print('Lukujen summa: ', summa)
print('Lukujen tulo: ', tulo)
print('Lukujen keskiarvo: ', keskiarvo)