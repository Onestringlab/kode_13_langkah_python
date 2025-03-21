class AkunBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo  # Private attribute

    def tampilkan_saldo(self):
        print(f"Saldo {self.nama}: Rp. {self.__saldo}")

    def tarik_saldo(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Penarikan Rp. {jumlah}")
        else:
            print("Saldo tidak mencukupi.")

# Membuat objek
akun1 = AkunBank("Andi", 500000)

# Mengakses metode
akun1.tampilkan_saldo()
akun1.tarik_saldo(200000)
akun1.tampilkan_saldo()