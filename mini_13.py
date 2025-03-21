# Sistem Perpustakaan dengan OOP dan File

import json

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.dipinjam = False

    def to_dict(self):
        return {"judul": self.judul, "penulis": self.penulis, "dipinjam": self.dipinjam}

class Perpustakaan:
    def __init__(self, file_nama="perpustakaan.json"):
        self.file_nama = file_nama
        self.daftar_buku = self.load_buku()

    def load_buku(self):
        try:
            with open(self.file_nama, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def simpan_buku(self):
        with open(self.file_nama, "w") as file:
            json.dump(self.daftar_buku, file, indent=4)

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku.to_dict())
        self.simpan_buku()

    def tampilkan_buku(self):
        for idx, buku in enumerate(self.daftar_buku, start=1):
            status = "Dipinjam" if buku["dipinjam"] else "Tersedia"
            print(f"{idx}. {buku['judul']} - {buku['penulis']} ({status})")

    def pinjam_buku(self, indeks):
        if 0 <= indeks < len(self.daftar_buku):
            if not self.daftar_buku[indeks]["dipinjam"]:
                self.daftar_buku[indeks]["dipinjam"] = True
                self.simpan_buku()
                print(f"Buku '{self.daftar_buku[indeks]['judul']}' berhasil dipinjam!")
            else:
                print("Buku ini sudah dipinjam.")
        else:
            print("Nomor buku tidak valid.")

# Program Utama
perpustakaan = Perpustakaan()

while True:
    print("\n1. Tambah Buku\n2. Tampilkan Buku\n3. Pinjam Buku\n4. Keluar")
    pilihan = input("Pilih opsi: ")

    if pilihan == "1":
        judul = input("Judul Buku: ")
        penulis = input("Penulis: ")
        buku_baru = Buku(judul, penulis)
        perpustakaan.tambah_buku(buku_baru)
        print("Buku berhasil ditambahkan!")

    elif pilihan == "2":
        perpustakaan.tampilkan_buku()

    elif pilihan == "3":
        perpustakaan.tampilkan_buku()
        try:
            indeks = int(input("Masukkan nomor buku yang ingin dipinjam: ")) - 1
            perpustakaan.pinjam_buku(indeks)
        except ValueError:
            print("Masukkan angka yang valid.")

    elif pilihan == "4":
        break