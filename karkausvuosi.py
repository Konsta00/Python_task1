vuosi = int(input('Anna vuosi (esim 2000): \n'))

if vuosi % 4 == 0:
    print(f'Vuosi {vuosi} on karkausvuosi!') 
elif vuosi % 100 == 0 and vuosi % 400 == 0:
    print(f'Vuosi {vuosi} on karkausvuosi')