import math

luoti = 13.3
naula = 32 * luoti
leiviska = 20 * naula

v = input('Anna leiviskät: ')
try:
    value = float(v)
    l = float(v) * float(leiviska)
except ValueError:
    v = input('Anna leiviskät: ')
    l = float(v) * float(leiviska)


v1 = input('Anna naulat: ')
try:
    value = float(v1)
    n = float(v1) * float(naula)
except ValueError:
    v2 = input('Anna naulat: ')
    n = float(v1) * float(naula)


v2 = input('Anna luodit: ')
try:
    value = float(v2)
    b = float(v2) * float(luoti)
except ValueError:
    v2 = input('Anna luodit: ')
    b = float(v2) * float(luoti)

print('Massa nykyisten mittojen mukaan: ')


g = float(l) + float(n) + float(b)
print(g, 'grammaa')

kg = g // 1000
g2 = g % 1000

print(kg, 'kg', g2, 'grammaa')
