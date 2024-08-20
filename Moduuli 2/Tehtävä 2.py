import math

sade = input("Syötä ympyrän säde: ")
sade_float = float(sade)
ala = math.pi * sade_float * sade_float
print("Pinta-ala on " + str(ala))