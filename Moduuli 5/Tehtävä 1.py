import random

nopat = input("Syötä noppien määrä: ")
nopat = int(nopat)
yht = 0


for i in range(nopat):
    yht += random.randint(1,6)

print(f"Summa {yht}")