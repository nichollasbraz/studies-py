def safePrint(arqNome):
    try:
        arqLeitura = open(arqNome, "r", encoding="UTF-8")
        arqCont = arqLeitura.readline()
        arqLeitura.close()

        print(f"{arqCont}")
    except:
        print("O arquivo {} não existe!".format(arqNome))

arqNome = input("Digite o nome do arquivo:\n> ")
safePrint(arqNome)
