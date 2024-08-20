vuosi = input("Syötä vuosi: ")
vuosi = int(vuosi)

if vuosi % 4 == 0 and vuosi % 100 != 0 or vuosi % 400 == 0:
    print("Hyvä vuosi")
else:
    print("Huono vuosi")