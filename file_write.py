# Membuka file dalam mode menulis
file = open("output.txt", "w")

# Menulis teks ke file
file.write("Halo, ini adalah data pertama!\n")
file.write("Python sangat menyenangkan.\n")

# Menutup file
file.close()

print("Data berhasil ditulis ke file output.txt")
