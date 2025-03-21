for i in range(1, 11):
    if i == 6:
        print("Loop berhenti di angka", i)
        break
    print(i)

for i in range(1, 6):
    if i == 3:
        print("Melewati angka", i)
        continue
    print(i)