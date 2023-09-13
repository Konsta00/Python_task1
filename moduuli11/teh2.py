# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. 
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
# Kirjoita aliluokille alustajat. 
# Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. 
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. 
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton 
# (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen 
# tunnin verran ja tulosta autojen matkamittarilukemat.
import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nykyinen_nopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = nykyinen_nopeus
        self.kuljettu_matka = 0

    def tulosta_ominaisuudet(self):
        print("Auton tiedot:")
        print("Rekisteritunnus:", self.rekisteritunnus)
        print("Huippunopeus:", self.huippunopeus, "km/h")
        print("Tämänhetkinen nopeus:", self.nykyinen_nopeus, "km/h")
        print("Kuljettu matka:", self.kuljettu_matka, "km")
        pass

    def kiihdyta(self, user_input):
        if  user_input > 0 and self.nykyinen_nopeus > 0:
            self.nykyinen_nopeus += user_input
        elif self.nykyinen_nopeus < 0:
            self.nykyinen_nopeus -= user_input

    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + (self.nykyinen_nopeus * float(tunnit))
        # print(f'Uusi nopeus: {self.kuljettu_matka}')

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, nykyinen_nopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus, nykyinen_nopeus)
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = nykyinen_nopeus
        self.akkukapasiteetti = akkukapasiteetti
        self.type = 'Sähköauto'

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, nykyinen_nopeus, tankin_tilavuus):
        super().__init__(rekisteritunnus, huippunopeus, nykyinen_nopeus)
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = nykyinen_nopeus
        self.tankin_tilavuus = tankin_tilavuus
        self.type = 'Polttomoottoriauto'

    

def main():

    tesla = Sähköauto("KSI-123", 310, random.randint(250, 300), 3000)
    ferrari = Polttomoottoriauto('ABC-123', 340, random.randint(250, 300), 90)

    tesla.kulje(3)
    ferrari.kulje(3)

    tesla.tulosta_ominaisuudet()
    print(f'Teslan akunkapasiteetti: {tesla.akkukapasiteetti} kwh')
    print(f'Tyyppi: {tesla.type}')

    ferrari.tulosta_ominaisuudet()
    print(f'Auton tankin tilavuus: {ferrari.tankin_tilavuus} litraa')
    print(f'Tyyppi: {ferrari.type}')


if __name__ == "__main__":
    main()