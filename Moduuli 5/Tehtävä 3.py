luku = input("Syötä luku: ")
luku = int(luku)

def testi(luku):
    if luku <= 1:
        return False
    if luku == 2:
        return True
    if luku % 2 == 0:
        return False

    for i in range(3, int(luku ** 0.5) + 1, 2):
        if luku % i == 0:
            return False
    return True

tof = testi(luku)

if tof:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")