class Hissi:
    def __init__(self, akerros, ykerros):
        self.akerros = akerros
        self.ykerros = ykerros
        self.nykyinen_kerros = akerros 

    def siirry_kerrokseen(self, kerros):
        if kerros > self.ykerros:
            print(f"Kerros {kerros} ei ole hissin toiminta-alueella.")
        elif kerros > self.nykyinen_kerros:
            self.kerros_ylös(kerros)
        elif kerros < self.nykyinen_kerros:
            self.kerros_alas(kerros)
        else:
            print(f"Hissi on jo kerroksessa {kerros}")

    def kerros_ylös(self, kerros):
        while self.nykyinen_kerros < kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi nousi kerrokseen {self.nykyinen_kerros}")

    def kerros_alas(self, kerros):
        while self.nykyinen_kerros > kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi laski kerrokseen {self.nykyinen_kerros}")

# Test the elevator
hissi = Hissi(0, 10)

hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(0)
hissi.siirry_kerrokseen(12)  # This is outside the elevator's range

print(f'Viimeisin kerros: {hissi.nykyinen_kerros}')
