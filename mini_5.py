# Penghitung Hari Antara Dua Tanggal
from datetime import datetime

def hitung_hari(tanggal1, tanggal2):
    t1 = datetime.strptime(tanggal1, "%Y-%m-%d")
    t2 = datetime.strptime(tanggal2, "%Y-%m-%d")
    selisih = abs((t2 - t1).days)
    print(f"Jumlah hari antara {tanggal1} dan {tanggal2} adalah {selisih} hari.")

tanggal1 = input("Masukkan tanggal pertama (YYYY-MM-DD): ")
tanggal2 = input("Masukkan tanggal kedua (YYYY-MM-DD): ")
hitung_hari(tanggal1, tanggal2)