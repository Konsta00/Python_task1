import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 60
        self.kuljettu_matka = 0

    def tulosta_ominaisuudet(self):
        print("Rekisteritunnus:", self.rekisteritunnus)
        print("Huippunopeus:", self.huippunopeus, "km/h")
        print("Tämänhetkinen nopeus:", self.nykyinen_nopeus, "km/h")
        print("Kuljettu matka:", self.kuljettu_matka, "km")

    def kiihdyta(self, user_input):
        if  user_input > 0 and self.nykyinen_nopeus > 0:
            self.nykyinen_nopeus += user_input
        elif self.nykyinen_nopeus < 0:
            self.nykyinen_nopeus -= user_input

    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + (self.nykyinen_nopeus * float(tunnit))

class Kilpailu: 
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot
        self.voittaja = ''

    def tunti_kuluu(self):
        for auto in self.autot: 
            if auto.kuljettu_matka < self.pituus_km:   
                auto.kiihdyta(random.randint(-10, 15))
                auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.autot:
            print(f'''
                  [REKISTERITUNNUS]---[HUIPPUNOPEUS]---[KULJETTUMATKA]
                  ------{auto.rekisteritunnus}--------------{auto.huippunopeus}-------------{auto.kuljettu_matka}-----
                  ''')
    
    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                self.voittaja = auto.rekisteritunnus
                return True
            else:
                return False

def main():    
    autolista = list()

    i = 0
    while i < 10:
        uusi_auto = Auto(f"ABC-{i}", random.randint(100, 200))
        autolista.append(uusi_auto)
        i += 1

    kilpailu = Kilpailu('Suuri romuralli', 8000, autolista)
    
    while True:
        if kilpailu.kilpailu_ohi():
            kilpailu.tulosta_tilanne()
            print(f'Kilpailun voitti auto: {kilpailu.voittaja}')
            break
        else:
            random.shuffle(kilpailu.autot)
            kilpailu.tunti_kuluu()
    
if __name__ == "__main__":
    main()