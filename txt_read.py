with open("data.txt", "r") as file:
    baris = file.readlines()
    print("Jumlah baris dalam file:", len(baris))