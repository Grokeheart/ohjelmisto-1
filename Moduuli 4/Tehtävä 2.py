while True:
    luku = input("Syötä tuumat: ")
    luku = float(luku)
    if luku < 0:
        break
    print(f"Senttimetreinä: {luku * 2.54}")