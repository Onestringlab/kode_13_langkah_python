def operasi_matematika(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else "Tidak bisa dibagi nol"

hasil = operasi_matematika(10, 5)
print("Hasil:", hasil)