class Anjing:
    def bersuara(self):
        print("Anjing menggonggong.")

class Kucing:
    def bersuara(self):
        print("Kucing mengeong.")

# Fungsi dengan polimorfisme
def suara_hewan(hewan):
    hewan.bersuara()

anjing = Anjing()
kucing = Kucing()

suara_hewan(anjing)
suara_hewan(kucing)