def kalkulator(a, b, operasi):
    if operasi == "+":
        return a + b
    elif operasi == "-":
        return a - b
    elif operasi == "*":
        return a * b
    elif operasi == "/":
        return a / b

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
operasi = input("Pilih operasi (+, -, *, /): ")
hasil = kalkulator(a, b, operasi)
print("Hasil:", hasil)