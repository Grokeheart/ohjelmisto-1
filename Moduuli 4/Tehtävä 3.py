min = 0
max = 0

while True:
    luku = input("Syötä luku: ")

    if luku:
        luku = float(luku)
    else:
        print(f"Min: {min} Max: {max}")
        break

    if min == 0 or luku < min:
        min = luku

    if max == 0 or luku > max:
        max = luku