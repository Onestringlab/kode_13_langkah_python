angka = int(input("Masukkan angka: "))
prima = True

if angka < 2:
    prima = False
else:
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            prima = False
            break

if prima:
    print(f"{angka} adalah bilangan prima")
else:
    print(f"{angka} bukan bilangan prima")