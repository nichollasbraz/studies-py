def numeroValido():
    n_1 = int(input("Digite um número de 1 a 9: "))

    while n_1 > 9 or n_1 < 1:
        n_1 = int(input("Entrada inválida!\nDigite um número de 1 a 9: "))

    n_2 = int(input("Digite um segundo número de 1 a 9: "))
    
    while n_2 > 9 or n_2 < 1:
        n_2 = int(input("Entrada inválida!\nDigite um número de 1 a 9: "))

    print("Números inseridos: {} e {}".format(n_1, n_2))

    return n_1, n_2
    
func = numeroValido()
