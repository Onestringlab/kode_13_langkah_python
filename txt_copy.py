with open("data.txt", "r") as sumber, open("salinan.txt", "w") as tujuan:
    for baris in sumber:
        tujuan.write(baris)

print("File berhasil disalin!")