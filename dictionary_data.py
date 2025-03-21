# Membuat dictionary
kontak = {
    "nama": "Rajo",
    "email": "rajo@email.com",
    "telepon": "081234567890"
}

# Mengakses nilai
print("Nama:", kontak["nama"])

# Menambahkan pasangan kunci-nilai
kontak["alamat"] = "Jakarta"

# Menghapus item
del kontak["email"]

# Iterasi dalam dictionary
for key, value in kontak.items():
    print(f"{key}: {value}")