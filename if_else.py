umur = 45

if umur < 12:
    print("Kamu masih anak-anak.")
elif umur < 18:
    print("Kamu masih remaja.")
elif umur < 60:
    print("Kamu sudah dewasa.")
else:
    print("Kamu sudah lansia.")

skor = int(input("Masukkan skor: "))

if skor >= 90:
    print("Nilai: A")
elif skor >= 80:
    print("Nilai: B")
elif skor >= 70:
    print("Nilai: C")
elif skor >= 60:
    print("Nilai: D")
else:
    print("Nilai: E")

hari = input("Masukkan nama hari: ").capitalize()

if hari in ["Sabtu", "Minggu"]:
    print("Hari libur!")
else:
    print("Hari kerja.")