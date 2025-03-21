# Pengonversi Mata Uang
tarif = {
    "USD": 1,
    "EUR": 0.85,
    "GBP": 0.75,
    "JPY": 110
}

def konversi_mata_uang(jumlah, dari_mata_uang, ke_mata_uang):
    if dari_mata_uang in tarif and ke_mata_uang in tarif:
        hasil = jumlah * (tarif[ke_mata_uang] / tarif[dari_mata_uang])
        print(f"{jumlah} {dari_mata_uang} adalah {hasil:.2f} {ke_mata_uang}")
    else:
        print("Mata uang tidak didukung.")

def main():
    jumlah = float(input("Masukkan jumlah uang: "))
    dari_mata_uang = input("Dari mata uang (USD, EUR, GBP, JPY): ")
    ke_mata_uang = input("Ke mata uang (USD, EUR, GBP, JPY): ")
    konversi_mata_uang(jumlah, dari_mata_uang, ke_mata_uang)

if __name__ == "__main__":
    main()