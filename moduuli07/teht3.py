lentokentat = lentokentat = {
    'EGLL': 'Heathrow lentokenttä',
    'LFPG': 'Charles de Gaullen lentokenttä',
    'KATL': 'Hartsfield-Jackson Atlanta lentokenttä',
    'RJTT': 'Tokion Hanedan lentokenttä',
    'ZBAA': 'Pekingin pääkaupungin lentokenttä',
}

while True:
    print('1. Lisää uusi lentokenttä')
    print('2. Hae lentokenttää ICAO-tunnisteella')
    print('3. Hae kaikki lentokentät')
    print('4. Lopeta ohjelma')

    input_valinta = input('[1|2|3|4]\n')

    if input_valinta == '1': 
        input_lentokentta_nimi = input('Anna lentokentän nimi: ')
        input_lentokentta_icao = input('Anna lentokentän ICAO-koodi: ')
        lentokentat[input_lentokentta_icao] = input_lentokentta_nimi
        print('Uusi lentokenttä lisätty.')
    elif input_valinta == '2':
        input_icao = input('Anna ICAO-koodi: ')
        if input_icao in lentokentat:
            print(f'Haetun lentokentän nimi on {lentokentat[input_icao]}')
        else:
            print('Lentokenttää ei löydy ICAO-koodilla.')
    elif input_valinta == '3':
        for i, icao in enumerate(lentokentat):
            if icao in lentokentat:
                print(f'{i+1}). {icao} | {lentokentat[icao]}')
    elif input_valinta == '4':
        break
    else:
        print('Virheellinen valinta. Valitse uudelleen.')        

