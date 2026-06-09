def meuGrep(filename, word):
    archive = open(filename, "r", encoding="UTF-8")
    lines = archive.readlines()
    archive.close()

    print("\nPalavra filtrada em {}: {}".format(filename, word))
    for line in lines:
        if word in line:
            print(line)
    
    return line

filename = input("Digite o nome do arquivo: ")
word = input("Digite a palavra a ser buscada:")
meuGrep(filename, word)
    