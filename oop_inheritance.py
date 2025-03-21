# Kelas Induk
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print("Hewan ini bersuara.")

# Kelas Anak yang mewarisi Hewan
class Kucing(Hewan):
    def bersuara(self):
        print(f"{self.nama} mengeong.")

# Membuat objek
kucing1 = Kucing("Milo")
kucing1.bersuara()