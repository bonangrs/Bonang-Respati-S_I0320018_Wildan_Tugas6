angka = 10
batas = 24
while angka <= batas:
    for i in range(2, angka):
        if angka % i == 0:
            print("%d bukan prima" % angka)
            break
    else:
        print("%d adalah bilangan prima" % angka)
    angka += 1
