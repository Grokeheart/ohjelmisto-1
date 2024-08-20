def muunnin(lista):
    uusiLista = []
    for numero in lista:
        if numero % 2 == 0:
            uusiLista.append(numero)
    return uusiLista

def main():
    lista = [1, 3, 4, 9, 12]
    print(lista)
    print(muunnin(lista))

if __name__ == '__main__':
    main()