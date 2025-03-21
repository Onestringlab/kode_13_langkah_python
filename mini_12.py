# To-Do List dengan File Handling
import json

FILE_NAMA = "tugas.json"

def load_tugas():
    try:
        with open(FILE_NAMA, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def simpan_tugas(tugas):
    with open(FILE_NAMA, "w") as file:
        json.dump(tugas, file, indent=4)

def tampilkan_tugas(tugas):
    if not tugas:
        print("Tidak ada tugas yang tersimpan.")
    else:
        print("\nDaftar Tugas:")
        for i, t in enumerate(tugas, start=1):
            print(f"{i}. {t}")

def tambah_tugas(tugas):
    tugas_baru = input("Masukkan tugas baru: ")
    tugas.append(tugas_baru)
    simpan_tugas(tugas)
    print("Tugas berhasil ditambahkan!")

def hapus_tugas(tugas):
    tampilkan_tugas(tugas)
    try:
        index = int(input("Masukkan nomor tugas yang akan dihapus: ")) - 1
        if 0 <= index < len(tugas):
            tugas.pop(index)
            simpan_tugas(tugas)
            print("Tugas berhasil dihapus!")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid.")

# Program Utama
tugas = load_tugas()

while True:
    print("\n1. Tambah Tugas\n2. Hapus Tugas\n3. Tampilkan Tugas\n4. Keluar")
    pilihan = input("Pilih opsi: ")

    if pilihan == "1":
        tambah_tugas(tugas)
    elif pilihan == "2":
        hapus_tugas(tugas)
    elif pilihan == "3":
        tampilkan_tugas(tugas)
    elif pilihan == "4":
        break