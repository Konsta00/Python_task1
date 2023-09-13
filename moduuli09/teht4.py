import random
from tabulate import tabulate

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

def main():
    
    autolista = list()

    i = 0
    while i < 10:
        uusi_auto = Auto(f"ABC-{i}", random.randint(100, 200))
        autolista.append(uusi_auto)
        i += 1

    while True:
        for auto in autolista:
            if auto.kuljettu_matka < 10000:
                auto.kiihdyta(random.randint(-10, 15))
                auto.kulje(1)
            else:
                print('Kilpailun voitti auto: ')
                # print(auto.tulosta_ominaisuudet())
                
                for auto in autolista:
                    print('[REKISTERITUNNUS]---[HUIPPUNOPEUS]---[KULJETTUMATKA]')
                    print(auto.rekisteritunnus, auto.huippunopeus, auto.kuljettu_matka)

                exit()

if __name__ == "__main__":
    main()