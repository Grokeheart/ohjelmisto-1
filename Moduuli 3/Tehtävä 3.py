from turtledemo.paint import switchupdown

sukupuoli = input("Syötä sukupuoli (M / N): ")
hemoglobiini = input("Syötä hemoglobiini: ")

hemoglobiini = float(hemoglobiini)

def laskuri(sukupuoli, hemoglobiini):
    if sukupuoli == "M":
        min = 134
        max = 195
    elif sukupuoli == "N":
        min = 117
        max = 175
    else:
        print("errör")
        return

    if hemoglobiini < min:
        print("Hemoglobiini on alhainen")
    elif hemoglobiini > min and hemoglobiini < max:
        print("Hemoglobiini on normaali")
    elif hemoglobiini > max:
        print("Hemoglobiini on korkea")

laskuri(sukupuoli, hemoglobiini)