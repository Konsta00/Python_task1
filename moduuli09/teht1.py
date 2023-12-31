class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 280
        self.kuljettu_matka = 3

    def tulosta_ominaisuudet(self):
        print("Auton tiedot:")
        print("Rekisteritunnus:", self.rekisteritunnus)
        print("Huippunopeus:", self.huippunopeus, "km/h")
        print("Tämänhetkinen nopeus:", self.nykyinen_nopeus, "km/h")
        print("Kuljettu matka:", self.kuljettu_matka, "km")

def main():
    uusi_auto = Auto("KSI-123", 299)
    uusi_auto.tulosta_ominaisuudet()

if __name__ == "__main__":
    main()