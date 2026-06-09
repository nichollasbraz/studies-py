def censura(arquivo_origem, arquivo_destino):
    arquivo = open(arquivo_origem, "r", encoding="UTF-8")
    conteudo = arquivo.read()
    arquivo.close()

    arquivo_saida = open(arquivo_destino, "w", encoding="UTF-8")

    palavras = conteudo.split()

    for palavra in palavras:
        if len(palavra) == 4:
            arquivo_saida.write("@@@@ ")
        else:
            arquivo_saida.write(palavra + " ")
    
    arquivo_saida.close()
    print("\nDuplicata de '{}' censurada com sucesso.\nArquivo destino: {}".format(arquivo_origem, arquivo_destino))

arquivo_origem = input("Escreva o nome do arquivo a ser censurado: ")
arquivo_destino = input("Escreva o nome da duplicata censurada: ")
censura(arquivo_origem, arquivo_destino)
