# Menghitung bunga majemuk
P = 1000  # Modal awal
r = 0.05  # Suku bunga 5% per tahun
n = 12  # Bunga dikapitalisasi 12 kali setahun
t = 5  # Selama 5 tahun

A = P * (1 + r/n) ** (n * t)
print("Total jumlah setelah 5 tahun:", round(A, 2))