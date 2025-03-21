def tampilkan_tugas(tugas):
    print("\nDaftar Tugas:")
    for indeks, item in enumerate(tugas, start=1):
        print(f"{indeks}. {item}")
    print()

def tambah_tugas(tugas):
    tugas_baru = input("Masukkan tugas baru: ")
    tugas.append(tugas_baru)
    print("Tugas ditambahkan.")

def hapus_tugas(tugas):
    tampilkan_tugas(tugas)
    indeks = int(input("Masukkan nomor tugas yang akan dihapus: ")) - 1
    if 0 <= indeks < len(tugas):
        tugas.pop(indeks)
        print("Tugas dihapus.")
    else:
        print("Nomor tugas tidak valid.")

def main():
    daftar_tugas = []
    while True:
        print("1. Tambah Tugas\n2. Hapus Tugas\n3. Tampilkan Tugas\n4. Keluar")
        pilihan = input("Pilih opsi: ")
        if pilihan == "1":
            tambah_tugas(daftar_tugas)
        elif pilihan == "2":
            hapus_tugas(daftar_tugas)
        elif pilihan == "3":
            tampilkan_tugas(daftar_tugas)
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()