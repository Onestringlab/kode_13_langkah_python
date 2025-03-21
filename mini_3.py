# Game Tebak Angka
import random

def tebak_angka():
    angka = random.randint(1, 100)
    tebakan = 0
    while True:
        tebakan = int(input("Tebak angka antara 1 dan 100: "))
        if tebakan < angka:
            print("Terlalu rendah!")
        elif tebakan > angka:
            print("Terlalu tinggi!")
        else:
            print("Selamat! Anda berhasil menebak angka tersebut.")
            break

if __name__ == "__main__":
    tebak_angka()