import math

def hintalaskuri(halkaisija, hinta):
    sade = halkaisija / 2
    ala = math.pi ** sade
    yksikkohinta = hinta / ala

    return yksikkohinta

def main():
    hinnat = []
    for i in range(2):
        halkaisija = input(f"Syötä pizzan {i+1}. halkaisija: ")
        hinta = input(f"Syötä pizzan {i+1}. hinta: ")
        hinnat.append(hintalaskuri(int(halkaisija), int(hinta)))

    if hinnat[0] > hinnat[1]:
        print(f"Pizza yksi on huokeampi.")
        print(f"Hinta per neliömetri: {hinnat[0]:.2f}")
    else:
        print(f"Pizza kaksi on huokeampi.")
        print(f"Hinta per neliömetri: {hinnat[0]:.2f}")

if __name__ == '__main__':
    main()