asematiedot = {
    "0100" : "Kentta1",
    "0200" : "Kentta2",
    "0300" : "Kentta3"
}

while True:
    toiminto = input("Haluatko hakea (h), tallentaa (t) vai lopettaa (l)?: ")

    if toiminto == "h":
        koodi = input("Syötä haettavan aseman koodi: ")
        if koodi in asematiedot:
            print(asematiedot[koodi])
        else:
            print("Asemalta kaaaaikuuuiivat kuuuulutukseeet")
    elif toiminto == "t":
        nimi = input("Syötä uuden aseman nimi: ")
        koodi = input("Syötä uuden aseman koodi: ")
        asematiedot[koodi] = nimi
    elif toiminto == "l":
        break