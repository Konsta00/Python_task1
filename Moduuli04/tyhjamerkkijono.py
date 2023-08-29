numerot = []  # Lista lukuja varten

while True:
    vastaus = input("Syötä luku (tyhjä merkkijono lopettaa): ")
    
    if vastaus == "":
        break  # Keskeytetään silmukka, kun syöte on tyhjä
    
    try:
        numero = float(vastaus)  # Muunnetaan syöte liukuluvuksi
        numerot.append(numero)
    except ValueError:
        print("Virheellinen syöte. Syötä kelvollinen luku tai tyhjä merkkijono.")

if numerot:
    min_number = min(numerot)
    max_number = max(numerot)
    
    print("Pienin luku:", int(min_number))
    print("Suurin luku:", int(max_number))
else:
    print("Et syöttänyt yhtään lukua.")
