# Kalkulator Bunga Majemuk
def hitung_bunga_majemuk(prinsipal, tingkat_bunga, waktu):
    jumlah = prinsipal * (1 + tingkat_bunga/100) ** waktu
    bunga = jumlah - prinsipal
    return bunga

prinsipal = float(input("Masukkan jumlah prinsipal: "))
tingkat_bunga = float(input("Masukkan tingkat bunga tahunan (dalam %): "))
waktu = float(input("Masukkan waktu (dalam tahun): "))
bunga = hitung_bunga_majemuk(prinsipal, tingkat_bunga, waktu)
print(f"Bunga majemuk setelah {waktu} tahun adalah: {bunga:.2f}")