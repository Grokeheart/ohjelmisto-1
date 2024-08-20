import random

pisteet = input("Syötä pisteiden määrä: ")
pisteet = int(pisteet)

luku = 0
osumat = 0

while luku < pisteet:
    luku += 1

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        osumat += 1

likiarvo = 4 * (osumat / pisteet)
print(likiarvo)
