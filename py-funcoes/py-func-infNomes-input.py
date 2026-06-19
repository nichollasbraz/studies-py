def infNomes():
    listaNomes = []

    while True:
        nome = input("Digite um nome:\n> ")
    
        if nome == "":
            break

        listaNomes.append(nome)

    contagem = {}

    for nome in listaNomes:
        if nome in contagem:
            contagem[nome] += 1
            
        else:
            contagem[nome] = 1
            
    for nome in contagem:
        if contagem[nome] > 1:
            print("'{}' aparece {} vezes.".format(nome, contagem[nome]))

        else:
            print("'{}' aparece {} vez.".format(nome, contagem[nome]))

infNomes()
    