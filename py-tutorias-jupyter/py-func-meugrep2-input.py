def meuGrep2(filename, word):
    archive = open(filename, "r", encoding="UTF-8")
    lines = archive.readlines()
    archive.close()
    filtered=[]

    for line in lines:
        if word in line:
            filtered.append(line)
        
    return filtered

filename = input("Digite o nome do arquivo: ")
word = input("Digite a palavra a ser buscada: ")

resultado = meuGrep2(filename, word)
if resultado:
    print("\nPalavra filtrada em '{}': {}".format(filename, word))
    for linha in resultado:
        print(linha, end="")
else:
    print("\nPalavra não encontrada.")
    