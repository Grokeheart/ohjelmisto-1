import random

def noppa():
    return random.randint(1,6)

def main():
    while True:
        luku = noppa()
        print(luku)
        if luku == 6:
            print("hell yeah")
            break

if __name__ == '__main__':
    main()