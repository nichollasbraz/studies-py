def fcopy(origem, destino):
    arquivo_origem = open(origem, "r", encoding="UTF-8")
    conteudo_origem = arquivo_origem.read()
    arquivo_origem.close()

    arquivo_destino = open(destino, "w", encoding="UTF-8")
    arquivo_destino.write(conteudo_origem)
    arquivo_destino.close()

    print("\nArquivo origem: {}\n Arquivo destino: {}".format(origem, destino))

origem = input("Escreva o nome do arquivo a ser copiado: ")
destino = input("Dê um nome para o novo arquivo: ")
fcopy(origem, destino)
