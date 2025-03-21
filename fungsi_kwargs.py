def tampilkan_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

tampilkan_info(nama="Rajo", umur=25, kota="Jakarta")