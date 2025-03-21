class Mahasiswa:
    def __init__(self, nama, jurusan, ipk):
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Jurusan: {self.jurusan}, IPK: {self.ipk}")

mhs1 = Mahasiswa("Budi", "Informatika", 3.8)
mhs1.tampilkan_info()