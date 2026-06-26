def divisores(arquivoNome):
    arquivo = open(arquivoNome, "r", encoding="UTF-8")
    conteudo = arquivo.readlines()
    arquivo.close()

    resultado = {}

    for linha in conteudo:
        numero = int(linha)
        listaDiv = []

        for i in range(1, numero):
            if numero % i == 0:
                listaDiv.append(i)
                
        resultado[numero] = listaDiv
    return resultado

arquivoNome = input("Digite o nome do arquivo:\n> ")
print(divisores(arquivoNome))
