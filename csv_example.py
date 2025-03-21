import csv

data = [
    ["Nama", "Usia", "Kota"],
    ["Andi", 25, "Jakarta"],
    ["Budi", 30, "Surabaya"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data berhasil disimpan di output.csv")
\end{python}