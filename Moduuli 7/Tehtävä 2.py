nimet = set()

while True:
    nimi = input("Syötä nimi: ")

    if nimi:
        if nimi in nimet:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
            nimet.add(nimi)
    else:
        break

for nimi in nimet:
    print(nimi)