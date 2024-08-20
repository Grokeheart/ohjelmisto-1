kanta = input("Syötä kanta: ")
korkeus = input("Syötä korkeus: ")

kanta = float(kanta)
korkeus = float(korkeus)

piiri = (kanta * 2) + (korkeus * 2)
ala = kanta * korkeus

print("Suorakulmion piiri on " + str(piiri))
print("Suorakulmion ala on " + str(ala))