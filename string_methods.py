teks = "  Belajar Python itu Mudah!  "

# Mengubah menjadi huruf kecil dan besar
print(teks.lower())
print(teks.upper())

# Menghapus spasi di awal dan akhir
print(teks.strip())

# Mengganti kata
print(teks.replace("Mudah", "Menyenangkan"))

# Memisahkan string
kata_kata = teks.split()
print(kata_kata)  # ['Belajar', 'Python', 'itu', 'Mudah!']