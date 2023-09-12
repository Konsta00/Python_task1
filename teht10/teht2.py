class Hissi:
    def __init__(self, akerros, ykerros, hissinumero):
        self.hissinumero = hissinumero
        self.akerros = akerros
        self.ykerros = ykerros
        self.nykyinen_kerros = akerros  # Start on the ground floor

    def siirry_kerrokseen(self, kerros):
        if kerros > self.ykerros:
            print(f"Kerros {kerros} ei ole hissin toiminta-alueella.")
        elif kerros > self.nykyinen_kerros:
            self.kerros_ylös(kerros)
        elif kerros < self.nykyinen_kerros:
            self.kerros_alas(kerros)
        else:
            print(f"Hissi {self.hissinumero} on jo kerroksessa {kerros}")

    def kerros_ylös(self, kerros):
        while self.nykyinen_kerros < kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi {self.hissinumero} nousi kerrokseen {self.nykyinen_kerros}")

    def kerros_alas(self, kerros):
        while self.nykyinen_kerros > kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi {self.hissinumero} laski kerrokseen {self.nykyinen_kerros}")

class Talo:
    def __init__(self, akerros, ykerros, hissi_lkm):
        self.akerros = akerros
        self.ykerros = ykerros
        self.hissi_lkm = hissi_lkm
        self.hissilista = []

    def aja_hissiä(self, hissi_nro, kohdekerros):
        if hissi_nro < len(self.hissilista):
            hissi = self.hissilista[hissi_nro]
            hissi.siirry_kerrokseen(kohdekerros)
        else:
            print(f"Hissi {hissi_nro} ei ole talossa.")

# Test the elevators in the building
hissi1 = Hissi(0, 10, 1)
hissi2 = Hissi(0, 10, 2)
hissi3 = Hissi(0, 10, 3)

talo = Talo(0, 10, 3)
talo.hissilista.extend([hissi1, hissi2, hissi3])

talo.aja_hissiä(2, 5)
