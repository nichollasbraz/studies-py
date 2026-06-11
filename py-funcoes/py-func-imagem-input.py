def inBoth(lista_1, lista_2):
    igual = []

    for elemento in lista_1:
        igual.append((elemento, elemento in lista_2))
        print(igual)
    return igual

lista_1 = input("Digite a primeira lista: ").strip()
lista_1 = lista_1.replace(",", "")
lista_1 = lista_1.split()

lista_2 = input("Digite a segunda lista: ").strip()
lista_2 = lista_2.replace(",", "")
lista_2 = lista_2.split()

resultado = inBoth(lista_1, lista_2)
print("\nLista com ambos valores: {}".format(resultado))

