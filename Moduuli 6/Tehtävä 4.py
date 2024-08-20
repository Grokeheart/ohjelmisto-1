def laskuri(lista):
    yht = 0
    for numero in lista:
        yht += numero
    return yht

def main():
    lista = [1, 3, 4, 9]
    print(laskuri(lista))

if __name__ == '__main__':
    main()