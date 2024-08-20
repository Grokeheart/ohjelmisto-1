import random

voittoluku = random.randint(1, 10)

while True:
    luku = input("Syötä luku: ")
    luku = int(luku)

    if luku == voittoluku:
        print("Oikein")
        break
    elif luku < voittoluku:
        print("Liian pieni arvaus")
    elif luku > voittoluku:
        print("Liian suuri arvaus")

