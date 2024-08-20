def muunnin(gallonat):
    return gallonat * 3.785

def main():
    while True:
        gallonat = input("Syötä gallonat: ")
        gallonat = int(gallonat)

        if gallonat >= 0:
            print(f"{gallonat} gallonaa on {muunnin(gallonat)} litraa")
        else:
            break

if __name__ == '__main__':
    main()