total = 0
while True:
    angka = int(input("Masukkan angka (jika memasukkan -1 maka akan berhenti): "))
    if angka == -1:
        break
    total += angka
print("Jumlah seluruh angka yang dimasukkan:", total)
