class Julkaisu():
    def __init__(self, nimi):
        self.nimi = nimi
    
    def tulosta_tiedot(self):
        pass

class Kirja(Julkaisu):
    def __init_(self, kirjailija, sivumäärä, nimi):
        super().__init__(nimi)
        self.nimi = nimi
        self.kirjailija = kirjailija
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f'Kirjan tiedot: \n Nimi: {self.nimi} \n Kirjailija: {self.kirjailija} \n Sivumäärä: {self.sivumäärä} ')

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.nimi = nimi
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f'Lehden tiedot: \n Nimi: {self.nimi} \n Päätoimittaja: {self.päätoimittaja}')        


if __name__ == '__main__':
    lehti = Lehti('Aku Ankka', 'Aki Hyyppä')
    kirja = Kirja('Hytti no6', 'Rosa Liksom', 200)

    lehti.tulosta_tiedot()
    kirja.tulosta_tiedot()
