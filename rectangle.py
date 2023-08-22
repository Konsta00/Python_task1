import math 
kanta = input('Valitse suorakulman kanta?')
korkeus = input('Valitse suorakulman korkeus?')

kanta_float = float(kanta)
korkeus_float = float(korkeus)

piiri = kanta_float*2 + korkeus_float*2
pintaala = kanta_float * korkeus_float

print('Suorakulmion piiri: ', piiri)
print('Suorakulmion pinta-ala: ', pintaala)

