luvut = []

while True:
    luku = input("Syötä luku: ")

    if luku:
        luku = int(luku)
    else:
        luvut.sort(reverse=True)
        y = 5
        for i in range(y):
            print(luvut[i])
        break

    luvut.append(luku)