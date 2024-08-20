kertoja = 1

while True:
    if kertoja == 5:
        print("Pääsy evätty.")
        break

    tunnus = input("Tunnus: ")
    salasana = input("Salasana: ")

    if tunnus != "python" or salasana != "rules":
        kertoja += 1
        print("Väärin")
    else:
        print("Tervetuloa")