import csv

with open("siswa.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if int(row[1]) > 80:  # Anggap kolom ke-2 adalah nilai
            print(row)