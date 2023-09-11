class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 60
        self.kuljettu_matka = 2000

    def tulosta_ominaisuudet(self):
        print("Auton tiedot:")
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
        # print(f'Uusi nopeus: {self.kuljettu_matka}')

            
def main():
    uusi_auto = Auto("KSI-123", 250)
    uusi_auto.kulje(1.5)

    uusi_auto.kiihdyta(30)
    uusi_auto.kiihdyta(70)
    uusi_auto.kiihdyta(50)
    print(f'Auton nopeus: {uusi_auto.nykyinen_nopeus}')

    print(f'Hätäjarru: {uusi_auto.nykyinen_nopeus - 200}')

    uusi_auto.tulosta_ominaisuudet()

if __name__ == "__main__":
    main()