tuuma = 2.54

vastaus = int(input('Ohjelma muuntaa tuumat senttimetriksi. \n Anna tuuma määrä: '))


if vastaus < 0:
    exit
elif vastaus > 0:
    sentit = vastaus * tuuma 
    print(f'{sentit} senttiä')
    vastaus = int(input('Ohjelma muuntaa tuumat senttimetriksi. \n Anna tuuma määrä: '))