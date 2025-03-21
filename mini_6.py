# Analisis File Log
def analisis_log(nama_file):
    with open(nama_file, "r") as file:
        baris_log = file.readlines()

    kesalahan = [baris for baris in baris_log if "ERROR" in baris]
    print(f"Jumlah baris total: {len(baris_log)}")
    print(f"Jumlah kesalahan: {len(kesalahan)}")

nama_file = input("Masukkan jalur file log: ")
analisis_log(nama_file)