# Manajemen Kontak dengan OOP dan File
import json

class Kontak:
    def __init__(self, nama, telepon, email):
        self.nama = nama
        self.telepon = telepon
        self.email = email

    def to_dict(self):
        return {"nama": self.nama, "telepon": self.telepon, "email": self.email}

class BukuKontak:
    def __init__(self, file_nama="kontak.json"):
        self.file_nama = file_nama
        self.kontak_list = self.load_kontak()

    def load_kontak(self):
        try:
            with open(self.file_nama, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def simpan_kontak(self):
        with open(self.file_nama, "w") as file:
            json.dump(self.kontak_list, file, indent=4)

    def tambah_kontak(self, kontak):
        self.kontak_list.append(kontak.to_dict())
        self.simpan_kontak()

    def tampilkan_kontak(self):
        for idx, kontak in enumerate(self.kontak_list, start=1):
            print(f"{idx}. {kontak['nama']} - {kontak['telepon']} - {kontak['email']}")

# Program Utama
buku_kontak = BukuKontak()

while True:
    print("\n1. Tambah Kontak\n2. Tampilkan Kontak\n3. Keluar")
    pilihan = input("Pilih opsi: ")

    if pilihan == "1":
        nama = input("Nama: ")
        telepon = input("Telepon: ")
        email = input("Email: ")
        kontak_baru = Kontak(nama, telepon, email)
        buku_kontak.tambah_kontak(kontak_baru)
        print("Kontak berhasil ditambahkan!")
    
    elif pilihan == "2":
        buku_kontak.tampilkan_kontak()

    elif pilihan == "3":
        break