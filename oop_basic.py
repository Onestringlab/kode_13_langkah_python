# Mendefinisikan kelas
class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def info(self):
        print(f"Mobil {self.merk} berwarna {self.warna}.")

# Membuat objek
mobil1 = Mobil("Toyota", "Merah")
mobil2 = Mobil("Honda", "Biru")

# Mengakses method
mobil1.info()
mobil2.info()