import random

def noppa(tahkot):
    return random.randint(1,tahkot)

def main():
    tahkot = input("Syötä tahkot: ")
    max = input("Syötä maksimi: ")
    tahkot = int(tahkot)
    max = int(max)

    while True:
        luku = noppa(tahkot)
        print(luku)
        if luku == max:
            print("hell yeah")
            break

if __name__ == '__main__':
    main()