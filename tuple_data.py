# Membuat tuple
warna = ("merah", "hijau", "biru")

# Mengakses elemen
print("Warna pertama:", warna[0])

# Mencoba mengubah isi tuple (akan menghasilkan error)
try:
    warna[0] = "kuning"
except TypeError:
    print("Tuple tidak dapat diubah!")

# Iterasi tuple
for w in warna:
    print("Warna:", w)