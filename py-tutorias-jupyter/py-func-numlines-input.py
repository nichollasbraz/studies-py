def meuIMC(peso, altura):
    indice = peso / (altura ** 2)

    if indice < 18.5:
        print("\nIMC: {:.1f}".format(indice))
        print("Abaixo do peso")
    elif 18.5 <= indice < 25:
        print("\nIMC: {:.1f}".format(indice))
        print("Peso normal")
    else:
        print("\nIMC: {:.1f}".format(indice))
        print("Acima do peso")

    return indice 

peso = float(input("Digite o peso do indivíduo: "))
altura = float(input("Digite a altura do indivíduo: "))
imc = meuIMC(peso,altura)
