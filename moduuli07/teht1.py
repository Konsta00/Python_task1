vuodenajat = ('Talvi', 'Kevät', 'Kevät', 'Kevät', 'Kesä', 'Kesä', 'Kesä', 'Syksy', 'Syksy', 'Syksy', 'Talvi', 'Talvi')

kuukauden_numero = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kuukauden_numero <= 12:
    vuodenaika = vuodenajat[kuukauden_numero - 1]
    
    print(f"Kuukausi numero {kuukauden_numero} on {vuodenaika}.")
else:
    print("Virheellinen kuukauden numero. Anna luku väliltä 1-12.")
