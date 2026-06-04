def buscarLinhas(filename, word):
    archive = open(filename, "r", encoding="UTF-8")
    lines = archive.readlines()
    archive.close
    filtered = []

    for l_1 in lines:
        if word in l_1:
            filtered.append(l_1)
        
    return filtered


filename = input("Digite o arquivo a ser procurado: ")
word = input("Digite a palavra a ser procurada: ")

result = buscarLinhas(filename, word)

if result:
    print("\nPalavra filtrada em '{}': {}".format(filename, word))
    for l_2 in result:    
        print(l_2, end="")

else:
    print("\nPalavra não encontrada.")
