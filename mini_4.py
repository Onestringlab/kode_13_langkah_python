# Pemeriksa Palindrom
def apakah_palindrom(teks):
    teks_bersih = ''.join([karakter.lower() for karakter in teks if karakter.isalnum()])
    return teks_bersih == teks_bersih[::-1]

teks = input("Masukkan kata atau frase: ")
if apakah_palindrom(teks):
    print("Ini adalah palindrom!")
else:
    print("Ini bukan palindrom.")