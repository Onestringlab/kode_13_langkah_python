# Pengonversi Suhu
def konversi_suhu(nilai, dari_skala, ke_skala):
    if dari_skala == "C" and ke_skala == "F":
        return (nilai * 9/5) + 32
    elif dari_skala == "F" and ke_skala == "C":
        return (nilai - 32) * 5/9
    else:
        return nilai

nilai = float(input("Masukkan nilai suhu: "))
dari_skala = input("Konversi dari (C/F): ")
ke_skala = input("Konversi ke (C/F): ")
hasil = konversi_suhu(nilai, dari_skala, ke_skala)
print(f"Suhu yang dikonversi adalah: {hasil:.2f} {ke_skala}")