def numeroValido(min, max):
    n_valido = int(input("Insira um valor entre {} e {}: ".format(min, max)))
   
    while n_valido <= min or n_valido >= max:
        print("O valor precisa ser maior que {} e menor que {}.".format(min, max))
        n_valido = int(input("Insira um valor entre {} e {}: ".format(min, max)))

    print("\nDentre os números:")
    print("{} {} {}".format(min, n_valido, max))

    return n_valido

min = int(input("Insira um valor mínimo: "))
max = int(input("Insira um valor máximo: "))

resultado = numeroValido(min, max)
