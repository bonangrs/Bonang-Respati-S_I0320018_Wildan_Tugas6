jmlhAngka = int(input("Masukkan jumlah angka yang ingin dirata-ratakan: "))
total = 0
i = 0

for i in range(jmlhAngka):
    angka = int(input("Masukkan angka ke-%d: " % (i+1)))
    total = total + angka

hasil = total / (i + 1)
print("Nilai rata-rata: %d" % hasil)
