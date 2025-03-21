# Membuka file dalam mode membaca
file = open("data.txt", "r")

# Membaca seluruh isi file
isi = file.read()
print("Isi file:")
print(isi)

# Menutup file setelah membaca
file.close()