# Generator Password Acak
import random
import string

def generate_password(panjang):
    karakter = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(karakter) for _ in range(panjang))
    return password

panjang = int(input("Masukkan panjang password yang diinginkan (minimal 1): "))
if panjang < 1:
    print("Panjang password harus minimal 1.")
else:
    print("Password yang dihasilkan:", generate_password(panjang))