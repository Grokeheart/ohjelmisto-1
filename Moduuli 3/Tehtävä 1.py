pituus = input("Syötä kuhan pituus: ")
pituus = float(pituus)

if pituus < 37:
    print("Kuha alimittainen. Heitä välittömästi veteen.")
    print(f"Pituudesta puuttuu {37 - pituus} cm")
else:
    print("Hyvä kala on")