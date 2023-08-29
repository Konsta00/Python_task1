attempts = 0
cUsername = 'python'
cPassword = 'rules'

while True: 
    username = str(input('Syötä käyttäjä tunnus:'))
    password = str(input('Syötä salasana:'))
    attempts += 1

    try:
        if attempts >= 5:
            print('Pääsy evätty, liika sisäänkirjautumis yrityksiä')
            break
        elif username != cUsername or password != cPassword and attempts < 5:
            print('Väärä käyttäjätunnus/salasana.')
        elif username == cUsername and password == cPassword:
            print(f'Tervetuloa käyttäjä: {username}')
            break        

    except ValueError:
        print('Virheellinen syöte. Syötä uudestaan käyttäjätunnus ja salasana')