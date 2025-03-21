class AkunBank:
    def __init__(self, nama, saldo, pin):
        self.nama = nama
        self.__saldo = saldo
        self.__pin = pin

    def tarik_saldo(self, jumlah, pin):
        if pin == self.__pin:
            if jumlah <= self.__saldo:
                self.__saldo -= jumlah
                print("Penarikan berhasil!")
            else:
                print("Saldo tidak cukup.")
        else:
            print("PIN salah!")

akun1 = AkunBank("Dina", 500000, 1234)
akun1.tarik_saldo(200000, 1234)
akun1.tarik_saldo(200000, 4321)